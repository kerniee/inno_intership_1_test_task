from aiogram import Dispatcher, types, Bot
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton


async def handle_determinant_btn_callback(callback_query: types.CallbackQuery):
    for s in Determinants.names:
        if str(hash(s)) == callback_query.data:
            await Determinants.bot.answer_callback_query(callback_query.id, "Нажата кнопка с текстом " + s)


class Determinants:
    names = []
    dp = None
    bot = None

    def __init__(self, bot: Bot, dp: Dispatcher):
        Determinants.dp = dp
        Determinants.bot = bot

        async def keyboard_handler(message: types.Message):
            markup = ReplyKeyboardMarkup(row_width=2)
            markup.add(
                *[InlineKeyboardButton("1", callback_data="1")]
                # str(hash(s))) for s in Determinants.names]
            )
            await message.answer("Определители болезни", reply_markup=markup)

        dp.register_message_handler(keyboard_handler, state='*', regexp="keyboard")


    def add_determinants(self, *args):
        Determinants.names.extend(args)
        self.dp.register_callback_query_handler(
            handle_determinant_btn_callback,
            lambda c: True
        # c.data in [str(hash(s)) for s in Determinants.names]
        )
