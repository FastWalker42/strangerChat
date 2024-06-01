from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.filters.is_private import IsPrivateFilter
import json
from aioredis import Redis

router = Router()
router.message.filter(IsPrivateFilter())


class ChosenAi(StatesGroup):
    chatgpt = State()
    image_generator = State()
    youtube_summary = State()


'''
@router.message(F.text)
async def set_state(message: types.Message, state: FSMContext):
    await state.set_state(Form.waiting_for_text)
    await message.answer("Введите текст для генерации изображения.")
'''


@router.message(F.text)
async def text_handler(message: types.Message, state: FSMContext):
    try:
        async with Redis() as r:
            queue_length = await r.llen('image_gen_queue')
            msg1 = await message.answer(f'⏳ В очереди: {queue_length+1}')
            await r.lpush('image_gen_queue', json.dumps(
                {"chat_id": message.chat.id, "prompt": f"{message.text}", "msg_id": msg1.message_id}
            ))
        await state.clear()  # Очистка состояния после выполнения
    except Exception as e:
        await message.answer("Не удалось сгенерировать изображение")
        print(e)
