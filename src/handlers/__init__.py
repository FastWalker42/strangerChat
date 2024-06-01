from aiogram import Dispatcher
from .commands import router as command_routes
from .text import router as text_routes
from .callback import router as callback_routes


def register_routes(dp: Dispatcher):
    dp.include_routers(command_routes, text_routes, callback_routes)
