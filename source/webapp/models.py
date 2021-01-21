from django.contrib.auth import get_user_model
from django.db import models


class File(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Название')
    file = models.FileField(upload_to='files', blank=False, null=False, verbose_name='файл')
    author = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='Автор')
    upload_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
