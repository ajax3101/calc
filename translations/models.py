from django.db import models
#from django.db.models.functions import Now

# Create your models here.


class Translate(models.Model):

    in_num = models.TextField(max_length=255, null=False, verbose_name='Введенная цифра')
    out_num = models.TextField(max_length=255, null=False, verbose_name='Конвертированная цифра')
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата время')
