import datetime

from aiogram.types import CallbackQuery
from filters import User
from loader import dp,data_base


# Echo bot
tunukafonlar = data_base.select_all_tunukafonlar()

tunukafonlar_royhati=[]
for tunuk in tunukafonlar:
    tunukafonlar_royhati.append(tunuk[1])

for tunuk_nomi in tunukafonlar_royhati:
    @dp.callback_query_handler(text=f"{tunuk_nomi}")
    async def bot_echo(message: CallbackQuery):
        tanlangan_tunuk = message.data
        tunuk_malumotlari=data_base.select_maxsulot(nomi=tanlangan_tunuk)
        nomi=tunuk_malumotlari[1]
        turi=tunuk_malumotlari[4]
        narxi = tunuk_malumotlari[3]
        rangi = tunuk_malumotlari[2]
        miqdori = tunuk_malumotlari[0]
        rasmi = tunuk_malumotlari[7]
        ism = message.from_user.first_name
        tg_id = message.from_user.id
        son = 1
        vaqt = datetime.datetime.now()
        data_base.add_sotib_olingan_max(ism=ism,nomi=nomi,tg_id=tg_id,miqdor=son,narxi=narxi,tur=turi,rangi=rangi,rasm=rasmi,vaqt=vaqt)
        await message.message.answer(text=f"{tanlangan_tunuk} Qo'shildi")
