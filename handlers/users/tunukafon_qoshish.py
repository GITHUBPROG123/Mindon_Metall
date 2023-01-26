from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import message, KeyboardButton, ReplyKeyboardMarkup
from django.contrib.sessions.backends import db
from django.forms import models

from keyboards.default.menu import asosiy_menu
from loader import dp

"""
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    nomi = models.CharField(max_length=30)
    rangi = models.CharField(max_length=30)
    narxi = models.IntegerField()
    miqdor = models.IntegerField()

    await message.answer(f"Salom, {message.from_user.full_name}! Botga hush kelibsiz", reply_markup=asosiy_menu)


"""

