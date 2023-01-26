from aiogram import types
from aiogram.types import InputFile,InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.default.menu import asosiy_menu
from loader import dp,data_base,bot

"""
tunukafonlar=data_base.select_maxsulot()
index=0
keys=[]
i=0
for tunuk in tunukafonlar:
    tunuk_nomi=tunuk[0]
    if i%2==0 and i != 0:
        index+=1
    if i%2 == 0:
        keys.append([KeyboardButton(text=f'{tunuk_nomi}')])
    else:
        keys[index].append(KeyboardButton(text=f'{tunuk_nomi}'))
    i+=1

asosiy_menu = ReplyKeyboardMarkup(keys, resize_keyboard=True)"""

@dp.message_handler(text='Tunukafon1')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    tunuk = data_base.select_maxsulot(nomi='Tunukafon1')
    tunuk_nomi = tunuk[1]
    tunuk_rangi = tunuk[2]
    tunuk_narxi = tunuk[3]
    tunuk_turi = tunuk[4]
    tunuk_rasmi = InputFile(path_or_bytesio=tunuk[7])
    
    await bot.send_photo(chat_id=user_id,
                         photo=tunuk_rasmi,
                         caption=f"Nomi: {tunuk_nomi}\n"
                                 f"Rangi: {tunuk_rangi}\n"
                                 f"Narxi: {tunuk_narxi}\n"
                                 f"Turi: {tunuk_turi}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Buyurtma berish',url='https://t.me/PROGRAM7UZ')
                                 ]
                             ]
                         ))

@dp.message_handler(text='Tunukafon2')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    tunuk = data_base.select_maxsulot(nomi='Tunukafon2')
    tunuk_nomi = tunuk[1]
    tunuk_rangi = tunuk[2]
    tunuk_narxi = tunuk[3]
    tunuk_turi = tunuk[4]
    tunuk_rasmi = InputFile(path_or_bytesio=tunuk[7])

    await bot.send_photo(chat_id=user_id,
                         photo=tunuk_rasmi,
                         caption=f"Nomi: {tunuk_nomi}\n"
                                 f"Rangi: {tunuk_rangi}\n"
                                 f"Narxi: {tunuk_narxi}\n"
                                 f"Turi: {tunuk_turi}\n",
                         reply_markup = InlineKeyboardMarkup(
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Buyurtma berish', url='https://t.me/PROGRAM7UZ')
                                ]
                            ]
                         ))


@dp.message_handler(text='Tunukafon3')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    tunuk = data_base.select_maxsulot(nomi='Tunukafon3')
    tunuk_nomi = tunuk[1]
    tunuk_rangi = tunuk[2]
    tunuk_narxi = tunuk[3]
    tunuk_turi = tunuk[4]
    tunuk_rasmi = InputFile(path_or_bytesio=tunuk[7])

    await bot.send_photo(chat_id=user_id,
                         photo=tunuk_rasmi,
                         caption=f"Nomi: {tunuk_nomi}\n"
                                 f"Rangi: {tunuk_rangi}\n"
                                 f"Narxi: {tunuk_narxi}\n"
                                 f"Turi: {tunuk_turi}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Buyurtma berish', url='https://t.me/PROGRAM7UZ')
                                 ]
                             ]

                         ))


@dp.message_handler(text='Tunukafon4')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    tunuk = data_base.select_maxsulot(nomi='Tunukafon4')
    tunuk_nomi = tunuk[1]
    tunuk_rangi = tunuk[2]
    tunuk_narxi = tunuk[3]
    tunuk_turi = tunuk[4]
    tunuk_rasmi = InputFile(path_or_bytesio=tunuk[7])

    await bot.send_photo(chat_id=user_id,
                         photo=tunuk_rasmi,
                         caption=f"Nomi: {tunuk_nomi}\n"
                                 f"Rangi: {tunuk_rangi}\n"
                                 f"Narxi: {tunuk_narxi}\n"
                                 f"Turi: {tunuk_turi}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Buyurtma berish', url='https://t.me/PROGRAM7UZ')
                                 ]
                             ]
                         ))

@dp.message_handler(text="G'isht")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    tunuk = data_base.select_maxsulot(nomi="G'isht")
    tunuk_nomi = tunuk[1]
    tunuk_rangi = tunuk[2]
    tunuk_narxi = tunuk[3]
    tunuk_turi = tunuk[4]
    tunuk_rasmi = InputFile(path_or_bytesio=tunuk[7])

    await bot.send_photo(chat_id=user_id,
                         photo=tunuk_rasmi,
                         caption=f"Nomi: {tunuk_nomi}\n"
                                 f"Rangi: {tunuk_rangi}\n"
                                 f"Narxi: {tunuk_narxi}\n"
                                 f"Turi: {tunuk_turi}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Buyurtma berish', url='https://t.me/PROGRAM7UZ')
                                 ]
                             ]
                         ))


@dp.message_handler(text="Gipsokarton")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    tunuk = data_base.select_maxsulot(nomi="Gipsokarton")
    tunuk_nomi = tunuk[1]
    tunuk_rangi = tunuk[2]
    tunuk_narxi = tunuk[3]
    tunuk_turi = tunuk[4]
    tunuk_rasmi = InputFile(path_or_bytesio=tunuk[7])

    await bot.send_photo(chat_id=user_id,
                         photo=tunuk_rasmi,
                         caption=f"Nomi: {tunuk_nomi}\n"
                                 f"Rangi: {tunuk_rangi}\n"
                                 f"Narxi: {tunuk_narxi}\n"
                                 f"Turi: {tunuk_turi}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Buyurtma berish', url='https://t.me/PROGRAM7UZ')
                                 ]
                             ]
                         ))



@dp.message_handler(text='Dasturchi')
async def bot_start(message: types.Message):
    await message.answer(text='@PROGRAM7UZ dasturchi Shuxratbek')

