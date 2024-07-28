# app/smm/models/message.py
from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тема', unique=True)
    text = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
