from aiogram import types
from loader import dp, bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


# Сохраняем фото подпод ноги
@dp.message_handler(content_types=['photo'])
async def bot_photo(message):
    photo_id = message.photo[2].file_id
    photo = await bot.get_file(photo_id)
    photo_path = photo.file_path
    await bot.download_file(photo_path, f"{message.message_id}_{message.chat.full_name}.png")


# Сохраняем документ подпод ноги
@dp.message_handler(content_types=['document'])
async def bot_doc(message):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"{message.message_id}_{message.document.file_name}")


# Делаем ответ полученным стикером
@dp.message_handler(content_types=['sticker'])
async def bot_sticker(message):
    sticker_id = message.sticker.file_id
    await bot.send_sticker(message.chat.id, sticker_id)


# Ответ на не прописанные действия
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def bot_error_response(message: types.Message):
    await message.answer(f"Извините я незнаю что это")
