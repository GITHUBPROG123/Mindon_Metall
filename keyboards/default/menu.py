from email import message

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from django.contrib.sessions.backends import db



asosiy_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Search'),
        ],
        [
            KeyboardButton(text='Tunukafon1'),
            KeyboardButton(text='Tunukafon2'),
        ],
        [
            KeyboardButton(text='Tunukafon3'),
            KeyboardButton(text='Tunukafon4'),
        ],
        [
            KeyboardButton(text='Biz haqimizda'),
            KeyboardButton(text='Dasturchi')
        ]
    ],
    resize_keyboard=True
)




