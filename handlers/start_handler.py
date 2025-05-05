from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from states.registration_state import Registration

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")
    await state.set_state(Registration.name)
    await message.answer("Ismingizni kiriting")
