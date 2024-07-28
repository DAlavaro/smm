# app/smm/models/client
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
