from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.localities import inline_kb_full
from loader import dp


def message_start():
    return ("Данный бот разработан с использованием",
            "сервиса Яндекс.Погода",
            "Для начала работы с ботом:",
            "Выберете населенный пункт из представленных на экране"
            )


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if 0 < message.date.hour < 6:
        text = "Доброй ночи, "
    elif 6 < message.date.hour < 11:
        text = "Доброе утро, "
    elif 11 < message.date.hour < 17:
        text = "Добрый день, "
    elif 17 < message.date.hour < 24:
        text = "Добрый вечер, "

    await message.answer(
        text + message.from_user.full_name + "!\n"
        "Выберите населенный пункт из представленных ниже",
        reply_markup=inline_kb_full()
                         )

    await message.answer("\n".join(message_start()))
