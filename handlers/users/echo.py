from aiogram import types
from loader import dp, bot
from utils.yandex_api.connect import connect


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(connect(message.text))


# Делаем ответ полученным стикером
@dp.message_handler(content_types=['sticker'])
async def bot_sticker(message):
    sticker_id = message.sticker.file_id
    await bot.send_sticker(message.chat.id, sticker_id)


# Ответ на не прописанные действия
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def bot_error_response(message: types.Message):
    await message.answer(f"Извините я незнаю что это")
