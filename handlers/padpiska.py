from aiogram import Router
from aiogram.enums import ChatMemberStatus
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import CHANNEL
from aiogram import Router

router = Router()


async def is_subscribed(bot, channel, user_id):
    user = await bot.get_chat_member(channel, user_id)
    return user.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]

@router.message(CommandStart())
async def start_handler(message: Message):
    if await is_subscribed(message.bot, CHANNEL, message.from_user.id):
        await message.answer("Xush kelibsiz!")
    else:
        await message.answer(f"{CHANNEL} ga obuna bo'ling")

@router.message()
async def echo_handler(message: Message):
    if not await is_subscribed(message.bot, CHANNEL, message.from_user.id):
        await message.answer("Botdan foydalanishdan oldin kanalga obuna bo‘ling!")
        return
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Bu xabarni nusxalab bo‘lmadi.")
