from aiogram import types
from aiogram.types import ContentType, message, KeyboardButton, ReplyKeyboardMarkup
from django.contrib.sessions.backends import db
from keyboards.default.menu import asosiy_menu
from loader import dp

# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    doc_id = message.document.file_id
    await message.answer(text=f"Dokument yuborildi idda")

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text='video yuborildi')

@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
        await message.video.download()
        await message.answer(text='video yuborildi')



