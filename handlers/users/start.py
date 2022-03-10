from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if 0 < message.date.hour < 6:
        await message.answer(f"Доброй ночи, {message.from_user.full_name}!")
    elif 6 < message.date.hour < 11:
        await message.answer(f"Доброе утро, {message.from_user.full_name}!")
    elif 11 < message.date.hour < 17:
        await message.answer(f"Доброго дня, {message.from_user.full_name}!")
    elif 17 < message.date.hour < 24:
        await message.answer(f"Доброго вечера, {message.from_user.full_name}!")
