from aiogram import types, Router
from aiogram.filters import Command
from src.filters.is_private import IsPrivateFilter
from src.keyboards import kb


router = Router()
router.message.filter(IsPrivateFilter())


'''
┃
┣ 🆔 <code>{channel.channel_id}</code>
┃ 
┣ 🌇 Тематика: <code>{channel.topic}</code>
┃
┣ 👤 Целевая аудитория: <code>{channel.auditory}</code>
┃
┗ 🎭

'''


@router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer(f"""
Приветствую, {message.from_user.first_name}!
┗👾🤖 Ты в лучшем ИИ-боте, и вот почему:

<b>Наш бот:</b>
┃
┣ 🎤 Принимает ГС в качестве ввода
┃
┗ 🔰🚀 Стабильный и живой 24/7

<b>Наш ИИ-ассистент:</b>
┃
┗ 🏆 DeepSeek - нейросеть, <a href="https://youtu.be/TIjyVI5Jd7A?si=hqhOfjJkvFy29PLs">превзошедшая GPT-4 в написании кода
</a>
<b>Наш генератор изображений:</b>
┃
┣ 🎯 Быстрый и безотказный
┃
┗ 🗽🔞 Генерация любых изображений <b>[НЕТ ЦЕНЗУРЫ]</b>

И все эти функции доступны вам <b>СОВЕРШЕННО БЕСПЛАТНО!</b>

<i>🧑‍💻 Разработчик готов разрулить любые проблемы и постоянно добавляет новые функции</i>
""", reply_markup=kb.my_contacts(), disable_web_page_preview=True)

