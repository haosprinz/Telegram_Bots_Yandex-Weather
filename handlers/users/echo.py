from datetime import datetime

from aiogram import types
from sqlalchemy.orm import sessionmaker

from data.config import ENGINE
from loader import dp
from utils.yandex_api.connect import connect
from data.models import Dialogs


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    session = sessionmaker(bind=ENGINE)()

    db_request_dialogs = Dialogs(
        user_text=message.text,
        user_id=int(message.from_user.id),
        user_name=message.from_user.full_name,
        date=datetime.now()
    )

    session.add(db_request_dialogs)
    session.commit()
    session.close()
    await message.answer(connect(message.text))


# Ответ на не прописанные действия
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def bot_error_response(message: types.Message):
    await message.answer(f"Извините я незнаю что это")
