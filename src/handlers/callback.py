from aiogram import types, Router, F
router = Router()


@router.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("lololol")
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )