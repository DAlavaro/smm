# app/smm/models/attempt.py
from django.db import models
from django.utils import timezone

from app.users.models import User


class MailAttempt(models.Model):

    STATUS_CHOICES = [
        ('success', 'Success'),
        ('failure', 'Failure'),
    ]

    mail = models.ForeignKey('Mail', on_delete=models.CASCADE, verbose_name='Рассылка')
    attempt_at = models.DateTimeField(default=timezone.now, verbose_name='Время попытки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='failure', verbose_name='Статус попытки')
    response = models.TextField(verbose_name='Ответ сервера', blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f"Attempt for {self.mail.name} at {self.attempt_at} - {self.status}"
