from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.registration_state import Registration
from database.db import add_user

router = Router()

@router.message(Registration.name)
async def process_name(message: Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer("Iltimos, faqat harflardan iborat ism kiriting!")
        return

    await state.update_data(name=message.text)
    await state.set_state(Registration.age)
    await message.answer("Yoshingizni kiriting")

@router.message(Registration.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Iltimos, yoshni raqam bilan kiriting!")
        return

    await state.update_data(age=int(message.text))
    await state.set_state(Registration.phone)
    await message.answer("Telefon raqamingizni kiriting")

@router.message(Registration.phone)
async def process_phone(message: Message, state: FSMContext):
    phone = message.text
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    referal = data.get("referal")

    add_user(name, age, phone, referal)

    await message.answer(f"✅ Ro‘yxatdan o‘tdingiz!\nIsm: {name}\nYosh: {age}\nTelefon: {phone}\nReferal: {referal}")
    await state.clear()
