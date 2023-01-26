
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp,data_base
from states.holatlar import Qidirish

# Echo bot
@dp.message_handler(text = 'Search')
async def bot_echo(message: types.Message):
    await message.answer(text="Maxsulot nomini kiriting")
    await Qidirish.qabul_qilish.set()

@dp.message_handler(state=Qidirish.qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    try:
        matn = message.text
        malumot = data_base.select_maxsulot(nomi=matn)
        await message.answer(text=f'Nomi: {malumot[1]}\n'
                                  f'Rangi: {malumot[2]}\n'
                                  f'Narxi: {malumot[3]}\n')

    except Exception as x:
        await message.answer(text="Bunday maxsulot nomi topilmadi")
        await state.finish()