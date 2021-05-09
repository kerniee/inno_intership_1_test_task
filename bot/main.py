import logging
import asyncio
import pprint
import re
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import StateFilter
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import text, bold, italic, code, pre, link
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode, \
    InlineKeyboardMarkup
from decouple import config
import prettytable as pt

import swagger_client.configuration
from bot.utils import MyStateFilter
from swagger_client import ApiClient, DeterminantProgress, AnswerQuestion
from swagger_client.rest import ApiException

import bot.messages as msg
from bot.models import Determinants, Me

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
REDIS_CONF = {
    "host": REDIS_IP,
    "port": REDIS_PORT,
    "password": REDIS_PASSWORD,
    "db": 5
}
storage_state = RedisStorage(**REDIS_CONF)

config = swagger_client.Configuration()
config.api_key_prefix["Authorization"] = "JWT"
config.host = "http://dev.teleagronom.com"
config.debug = DEBUG
api_client = ApiClient(config)

MyStateFilter.api_client = api_client

dp = Dispatcher(bot, storage=storage_state)
dp.filters_factory.unbind(StateFilter)
dp.filters_factory.bind(MyStateFilter, exclude_event_handlers=[
    dp.errors_handlers,
    dp.poll_handlers,
    dp.poll_answer_handlers,
])
dp.middleware.setup(LoggingMiddleware())

# def _auth(self, token: str):
#     self.default_headers["Authorization"] = f"Bearer {token}"
#
#
# setattr(
#     swagger_client.ApiClient,
#     "set_auth_token",
#     _auth
# )
auth_api = swagger_client.AuthApi(api_client)
progress_api = swagger_client.V1progressApi(api_client)
# barley_determinant = swagger_client.BarleyDeterminantControllerApi(api_client)

determinants = Determinants(bot, dp, api_client)
me = Me(bot, dp, auth_api)


class States(StatesGroup):
    logout = State()
    login_enter_username = State()
    login_enter_password = State()
    logged = State()
    enter_new_det_name = State()


@dp.message_handler(commands='start', state='*')
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    await message.answer(msg.hello, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands='help', state='*')
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    await message.answer(msg.help)


@dp.message_handler(commands='login', state='*')
async def cmd_login(message: types.Message):
    # Set state
    await States.login_enter_username.set()

    await message.answer(msg.enter_name, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=States.login_enter_username)
async def login_username_read(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    # Set state
    await States.login_enter_password.set()

    await message.answer(msg.enter_password)


@dp.message_handler(state=States.login_enter_password)
async def login_password_read(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
        req = message.answer(msg.logging)
        try:
            resp = auth_api.auth_jwt_create_create({
                "username": data['username'],
                "password": data['password'],
            })
        except ApiException:
            answer = await req
            await answer.edit_text(msg.logging_failed)
            await state.finish()
            return
        data["token"] = resp.access
        save_token = storage_state.set_data(chat=message.chat.id, user=message.from_user.id,
                                            data={"token": resp.access})
        # api_client.default_headers["authorization"] = f"JWT {resp.access}"
    answer = await req
    await answer.edit_text(msg.logging_completed)
    await States.logged.set()
    markup = ReplyKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(msg.my_determinants),
        InlineKeyboardButton(msg.new_determinant)
    )
    await save_token
    await message.answer(msg.choose_button, reply_markup=markup)


@dp.message_handler(commands=["menu"], state=States.logged)
async def menu(message: types.Message):
    markup = ReplyKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(msg.my_determinants),
        InlineKeyboardButton(msg.new_determinant)
    )
    await message.answer(msg.choose_button, reply_markup=markup)


@dp.message_handler(commands=["determinant"], state=States.logged)
async def show_determinant(message: types.Message, state: FSMContext):
    items = message.text.split()
    if len(items) == 2:
        all_determinants = progress_api.progress_list()
        name_to_id = dict(
            [(res.name, res.id) for res in all_determinants.results]
        )
        if items[1] in name_to_id:
            await show_determinant_in_progress(name_to_id[items[1]], message, state)
        else:
            await message.answer(msg.no_determinant_with_name)
    else:
        await message.answer(msg.wrong_args, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(regexp=f'^{msg.my_determinants}', state=States.logged)
async def my_determinants_button(message: types.Message, state: FSMContext):
    all_determinants = progress_api.progress_list()
    # logging.info(str(all_determinants))
    table = pt.PrettyTable(['Название', 'Дата создания', 'Болезнь', 'Статус'])
    table._max_width = {
        'Название': 20,
        'Дата создания': 20,
        'Болезнь': 20,
        'Статус': 20
    }
    table.align['Название'] = 'l'
    for s in all_determinants.results:
        row = [s.name,
               datetime.strptime(s.created_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d.%m.%Y"),
               s.disease.name if hasattr(s, 'disease') and hasattr(s.disease, 'name') else '',
               'Расчитан' if s.disease else "В процессе"]
        table.add_row(row)
    await message.answer(f'```{table}```', parse_mode=ParseMode.MARKDOWN_V2)


@dp.message_handler(regexp=f'^{msg.new_determinant}', state=States.logged)
async def new_determinant_show_layout(message: types.Message, state: FSMContext):
    # try:
    #     resp2 = barley_determinant.get_all_using_get()
    # except ApiException:
    #     pass
    markup = ReplyKeyboardMarkup(row_width=2)
    markup.add(
        *[InlineKeyboardButton(s, callback_data=str(hash(s))) for s in determinants.names]
    )

    await message.answer(msg.choose_new_det_type, reply_markup=markup)


@dp.message_handler(lambda message: message.text in determinants.names, state=States.logged)
async def new_determinant_type_button(message: types.Message, state: FSMContext):
    await States.enter_new_det_name.set()

    async with state.proxy() as data:
        data["id"] = determinants.id_from_name(message.text)

    await message.answer(msg.choose_new_det_name, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=States.enter_new_det_name)
async def new_determinant_name_entered(message: types.Message, state: FSMContext):
    await States.logged.set()

    async with state.proxy() as data:
        res = progress_api.progress_create(**{
            "determinant": data["id"],
            "name": message.text,
            "user": me.id
        })

    await show_determinant_in_progress(res.id, message, state)


async def show_determinant_in_progress(_id: int, message: types.Message, state: FSMContext):
    current_item = progress_api.progress_current_item_retrieve(_id)

    _text, inline_kb = generate_text(current_item, _id)

    if len(_text) > 4096:
        for x in range(0, len(_text), 4096):
            new_message = await message.answer(_text[x:x + 4096], parse_mode=ParseMode.MARKDOWN, reply_markup=inline_kb)
    else:
        new_message = await message.answer(_text, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_kb)
    async with state.proxy() as data:
        data[f"add_det__{_id}"] = {
            "chat_id": new_message.chat.id,
            "message_id": new_message.message_id
        }


def generate_text(current_item, _id):
    progress = progress_api.progress_retrieve(_id)
    name = progress.name
    inline_kb = None
    if current_item["type"] == "question":
        _text = text(
            f'Имя: {name}\n',
            bold(str(current_item["number"]).strip()),
            f'. {current_item["title"]}\n',
            'Варианты ответа:\n',
            '\n'.join(["    " + i["text"] for i in current_item["answers"]]), sep=''
        )
        btns = [
            InlineKeyboardButton(ans["text"], callback_data=f'add_det__{_id}_{ans["number"]}')
            for ans in current_item["answers"]
        ]
        inline_kb = InlineKeyboardMarkup(row_width=1).add(*btns)
    elif current_item["type"] == "disease":
        progress = progress_api.progress_retrieve(_id)
        pp = pprint.PrettyPrinter(indent=1, width=200)
        _text = text(f"Название болезни: {current_item['title']}\n"
                     f"Больше информации на",
                     link("сайте", f'http://dev.teleagronom.com/determinant/{progress.determinant["id"]}/{_id}'))
        # _text += progress.disease.to_str()
    else:
        raise Exception(f"Unknown type: {current_item['type']}")
    return _text, inline_kb


@dp.callback_query_handler(lambda c: c.data.startswith('add_det__'), state=States.logged)
async def process_callback_button1(callback_query: types.CallbackQuery, state: FSMContext):
    match = re.match(r"add_det__(.*)_(.*)", callback_query.data)
    if match:
        _id, number = map(int, match.groups())
        async with state.proxy() as data:
            res = data[f"add_det__{_id}"]
        current_item = progress_api.progress_answer_question_create(AnswerQuestion(
            number
        ), _id)
        _text, inline_kb = generate_text(current_item, _id)
        await bot.edit_message_text(_text, **res, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_kb)
    else:
        raise Exception("Invalid button data")
        # await bot.send_message(callback_query.from_user.id, 'Нажата кнопка!')


@dp.message_handler()
async def not_logged(message: types.Message):
    await message.answer(msg.not_logged)


# @dp.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message, state):
#     await message.reply()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    asyncio.run(dp.storage.close())
    asyncio.run(dp.storage.wait_closed())
