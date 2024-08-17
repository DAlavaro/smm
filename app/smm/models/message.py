# app/smm/models/message.py
from django.db import models

from app.users.models import User


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тема', unique=True)
    text = models.TextField(verbose_name='Текст сообщения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
