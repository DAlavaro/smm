# app/smm/models/client
from django.db import models

from app.users.models import User


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
