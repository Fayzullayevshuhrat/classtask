from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from states.registration_state import Registration

CHANNEL = "@shukhratfayzullayev"

async def check_subscription(bot, user_id, channel_username):
    member = await bot.get_chat_member(chat_id=channel_username, user_id=user_id)
    return member.status in ("member", "creator", "administrator")

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext, bot: Bot) -> None:
    args = message.text.split()
    referal = args[1] if len(args) > 1 else None

    await state.update_data(referal=referal)


    is_subscribed = await check_subscription(bot, message.from_user.id, CHANNEL)
    if not is_subscribed:
        await message.answer(f"❗ Botdan foydalanish uchun {CHANNEL} ga obuna bo‘ling!")
        return


    await message.answer(f"Hello, {message.from_user.full_name}!")
    await state.set_state(Registration.name)
    await message.answer("Ismingizni kiriting")
