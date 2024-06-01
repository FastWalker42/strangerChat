from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def my_contacts():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="📱 Реклама / поддержка / заказать бота",
        url="https://t.me/fastwalkerrr")
    )
    builder.row(types.InlineKeyboardButton(
        text="♨️ GitHub", url="https://github.com/FastWalker42")
    )
    return builder.as_markup()


def main_menu():
    builder = InlineKeyboardBuilder()

    btns = {
        "ai_assistant": "🧠 GPT-4 ассистент",
        "img_gen": "🖼 Генератор изображений",
        "summarizer": "📮 Пересказ видео с YouTube",
        "bingai": "🧿 Поиск изображений Bing",
        "shop": "📚 Магазин",
        "support": "💵 Поддержать автора"
    }

    [builder.row(types.InlineKeyboardButton(text=btns[i], callback_data=i)) for i in btns]
    return builder.as_markup()


def settings_img_gen():
    builder = InlineKeyboardBuilder()
    btns = {
        'vertical': '📱 Вертикальное',
        'square': '📺 Квадрат',
        'horizontal': '🖥 Горизонтальное'
    }
    [builder.row(types.InlineKeyboardButton(text=btns[i], callback_data=i)) for i in btns]
    return builder.as_markup()
# '512x768' or '512x512' or '768x512'
