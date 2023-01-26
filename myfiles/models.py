from django.db import models

# Create your models here.
class Tur(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi
class Maxsulotlar(models.Model):
    nomi = models.CharField(max_length=30)
    tur = models.ForeignKey(Tur,on_delete=models.CASCADE)
    rangi = models.CharField(max_length=30)
    narxi = models.IntegerField()
    miqdor = models.IntegerField()
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)


class Sotib_olingan_max(models.Model):
    ism = models.CharField(max_length=30)
    tg_id = models.IntegerField()
    nomi = models.CharField(max_length=30)
    tur = models.CharField(max_length=30)
    rangi = models.CharField(max_length=30)
    narxi = models.IntegerField()
    miqdor = models.IntegerField()
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)


