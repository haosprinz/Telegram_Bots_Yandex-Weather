from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp, bot
from utils.yandex_api.dictionary_cities import dictionary
from utils.yandex_api.connect import connect


def inline_kb_full():
    keyboard = InlineKeyboardMarkup()
    for key in dictionary.keys():
        keyboard.insert(InlineKeyboardButton(
            text=key,
            callback_data=f"city_{key}"))

    return keyboard


@dp.callback_query_handler(text_contains="city_")
async def process_callback(call: CallbackQuery):
    data = call.data.split("_")[1]
    await bot.send_message(call.from_user.id, text=connect(data))
