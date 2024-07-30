# app/smm/models/mail.py
from django.db import models


class Mail(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название рассылки', unique=True)
    time = models.DateField(verbose_name='Время начала отправки рассылки')
    count = models.PositiveIntegerField(verbose_name='Количество рассылок')

    PERIOD_CHOICES = (
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    )
    period = models.CharField(max_length=255, choices=PERIOD_CHOICES, verbose_name='Периодичность рассылки')

    STATUS_CHOICES = (
        ('active', 'Активна'),
        ('inactive', 'Не активна'),
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, verbose_name='Статус рассылки')
    message = models.ForeignKey('smm.Message', on_delete=models.CASCADE, verbose_name='Сообщение')
    clients = models.ManyToManyField('smm.Client', related_name='mails', verbose_name='Клиенты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
