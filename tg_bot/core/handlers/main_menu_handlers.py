from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.keyboards.main_menu_keyboards import main_menu_keyboard


router: Router = Router()


@router.message(Command(commands="start"))
async def cmd_start(message: Message) -> None:
    await message.answer(
        text="Запустите терминал",
        reply_markup=main_menu_keyboard
    )
    await message.delete()
