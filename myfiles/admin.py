from django.contrib import admin
from myfiles.models import *

# Register your models here.

class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']
class AdminMax(admin.ModelAdmin):
    list_display = ['id','nomi','rangi','tur','narxi','vaqt']
admin.site.register(Tur,AdminTur)
admin.site.register(Maxsulotlar, AdminMax)
"""
class AdminSotib_max(admin.ModelAdmin):
    list_display = ['id','ism','tg_id','nomi','rangi','miqdor','tur','narxi','vaqt']
admin.site.register(Sotib_olingan_max,AdminSotib_max)
"""


