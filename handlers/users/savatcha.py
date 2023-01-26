import datetime

from aiogram import types
from aiogram.types import CallbackQuery, Message, InputFile, InlineKeyboardMarkup

from loader import dp, data_base, bot


@dp.message_handler(text=f'Savatcha')
async def bot_echo(message: Message):
        user_id = message.from_user.id
        
        savatchadagi_max = data_base.select_sotib_olingan_maxlar(tg_id = user_id)
        savatchadagi_max_roy = []
        for max in savatchadagi_max:
            user_id = message.from_user.id
            max_nomi = max[1]
            max_rangi = max[2]
            max_narxi = max[3]
            max_turi = max[4]
            max_rasmi = InputFile(path_or_bytesio=max[7])

            await bot.send_photo(chat_id=user_id,
                                 photo=max_rasmi,
                                 caption=f"Nomi: {max_nomi}\n"
                                         f"Rangi: {max_rangi}\n"
                                         f"Narxi: {max_narxi}\n"
                                         f"Turi: {max_turi}",
                                 )
      




