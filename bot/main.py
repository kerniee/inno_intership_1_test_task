import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup
from decouple import config

import swagger_client.configuration
from swagger_client.rest import ApiException

import bot.messages as msg
from bot.models import Determinants

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")
REDIS_IP = config("REDIS_IP")
REDIS_PORT = config("REDIS_PORT", cast=int, default=6379)
REDIS_PASSWORD = config("REDIS_PASSWORD_MASTER")
DEBUG = config("TELEGRAM_BOT_DEBUG", cast=bool, default=False)

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
storage = RedisStorage(
    host=REDIS_IP,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    db=5)
dp = Dispatcher(bot, storage=storage)
determinants = Determinants(bot, dp)
determinants.add_determinants(*(
    "Картофель",
    "Морковь",
    "Рожь",
    "Ячмень"
))

config = swagger_client.Configuration()
config.api_key_prefix["token"] = "BEARER"
config.debug = DEBUG
api_client = swagger_client.ApiClient()


def _auth(self, token: str):
    self.default_headers["Authorization"] = f"Bearer {token}"


setattr(
    swagger_client.ApiClient,
    "set_auth_token",
    _auth
)

auth_api = swagger_client.AuthenticationControllerApi(api_client)
barley_determinant = swagger_client.BarleyDeterminantControllerApi(api_client)


class States(StatesGroup):
    logout = State()
    login_enter_username = State()
    login_enter_password = State()
    logged = State()


@dp.message_handler(commands='start', state='*')
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    await message.reply(msg.hello)


@dp.message_handler(commands='login', state='*')
async def cmd_login(message: types.Message):
    # Set state
    await States.login_enter_username.set()

    await message.reply(msg.enter_name)


@dp.message_handler(state=States.login_enter_username)
async def login_username_read(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    # Set state
    await States.login_enter_password.set()

    await message.reply(msg.enter_password)


@dp.message_handler(state=States.login_enter_password)
async def login_password_read(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
        req = message.reply(msg.logging)
        try:
            resp = auth_api.login_using_post({
                "password": data['password'],
                "username": data['username']
            })
        except ApiException:
            answer = await req
            await answer.edit_text(msg.logging_failed)
            await States.logout.set()
            return
        data["token"] = resp.token
        api_client.default_headers["Authorization"] = f"Bearer {resp.token}"
    answer = await req
    await answer.edit_text(msg.logging_completed)
    await States.logged.set()


# @dp.message_handler(state='*', regexp="keyboard")
# async def any_(message: types.Message, state: FSMContext):
#     # resp = auth_api.login_using_post({
#     #     "password": "string",
#     #     "username": "string"
#     # })
#     # api_client.default_headers["Authorization"] = f"Bearer {resp.token}"
#     # api_client.set_auth_token(resp.token)
#     # try:
#     #     resp2 = barley_determinant.get_all_using_get()
#     # except ApiException:
#     #     pass
#     markup = ReplyKeyboardMarkup(row_width=2)
#     markup.add(
#         *[InlineKeyboardButton(s, callback_data=str(hash(s))) for s in determinants.names]
#     )
#
#     await message.answer("Определители болезни", reply_markup=markup)

# @dp.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message, state):
#     await message.reply()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    asyncio.run(dp.storage.close())
    asyncio.run(dp.storage.wait_closed())
