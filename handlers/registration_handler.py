from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from states.registration_state import Registration
from database.db import add_user

router = Router()


@router.message(Registration.name, Command("help"))
async def echo_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Faqat harflardan iborat ism kiriting")

@router.message(Registration.name)
async def echo_handler(message: Message, state: FSMContext) -> None:
    name = message.text

    if name.isalpha():
        await message.answer("Sizining ismingiz qabul qilindi")
        await state.set_state(Registration.age)
        add_user(name)

    else:
        await message.answer("Siz notogri ism kiritidingiz, waytadan urining")

@router.message(Command("help"))
async def echo_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Tez orada 103 keladi!")
