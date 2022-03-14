from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.inline.localities import inline_kb_full
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))
    await message.answer(f"Выберите населенный пункт из представленных ниже", reply_markup=inline_kb_full())
