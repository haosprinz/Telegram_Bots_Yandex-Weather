from environs import Env
from sqlalchemy import create_engine

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов

# webhook settings
WEBHOOK_HOST = env.str("WEBHOOK_HOST")
WEBHOOK_PATH = env.str("WEBHOOK_PATH")
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = env.str("WEBAPP_HOST")
WEBAPP_PORT = env.str("WEBAPP_PORT")

# Database
DB_NAME = env.str("DATABASE_NAME")
DB_HOST = env.str("DATABASE_HOST")
DB_PASSWORD = env.str("DATABASE_PASSWORD")
DB_USER = env.str("DATABASE_USER")
DB_ENGINE = env.str("DATABASE_ENGINE")

# Yandex Api
YANDEX_URL = env.str("YANDEX_URL")
YANDEX_KEY = env.str("YANDEX_KEY")
YANDEX_VALUE = env.str("YANDEX_VALUE")

ENGINE = create_engine('{0}://{1}:{2}@{3}/{4}'.format(DB_ENGINE, DB_USER,
                                                      DB_PASSWORD, DB_HOST, DB_NAME))

CREATEBDENGINE = create_engine('{0}://{1}:{2}@{3}'.format(DB_ENGINE, DB_USER,
                                                          DB_PASSWORD, DB_HOST))
