import logging
from aiogram import executor

from data.db import create_tables, create_db
import data.config as cfg
from loader import dp, bot
from aiogram.utils.executor import start_webhook
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Создаем базу данных
    try:
        create_db()
    except:
        logging.info('БД уже создана')

    # Создаем таблицы в базе данных
    try:
        create_tables()
    except:
        logging.info('Таблица уже создана')

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def on_startup_webhook(dispatcher):
    await on_startup(dispatcher)
    await bot.set_webhook(cfg.WEBHOOK_URL)


async def on_shutdown_webhook(dispatcher):
    logging.warning('Shutting down..')

    for admin in cfg.ADMINS:
        await dispatcher.bot.send_message(admin, "Бот выключен")
        logging.warning('bot offline')

    # Remove webhook
    await bot.delete_webhook()

    # Close DB connection
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

    logging.warning('Bye!')

if __name__ == '__main__':
    if cfg.WEBHOOK_HOST == "":
        executor.start_polling(dp, on_startup=on_startup)
    else:
        start_webhook(
            dispatcher=dp,
            webhook_path=cfg.WEBHOOK_PATH,
            on_startup=on_startup_webhook,
            on_shutdown=on_shutdown_webhook,
            skip_updates=True,
            host=cfg.WEBAPP_HOST,
            port=cfg.WEBAPP_PORT
        )