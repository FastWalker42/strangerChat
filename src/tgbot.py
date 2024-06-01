from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from src import load_config

from src.handlers import register_routes
from src.middlewares.config import ConfigMiddleware

config = load_config(".env")

WEBHOOK_PATH = f"/bot/{config.tg.token}"
WEBHOOK_URL = config.tg.webhook_url + WEBHOOK_PATH

storage = MemoryStorage()

bot = Bot(token=config.tg.token, parse_mode="HTML")
dp = Dispatcher(storage=storage)

# Register middlewares
dp.update.middleware(ConfigMiddleware(config))

# Register routes
register_routes(dp)
