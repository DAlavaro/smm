# app/smm/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

from app.users.models import User


class Mail(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    name = models.CharField(max_length=255)
    time = models.DateField()
    count = models.PositiveIntegerField()
    period = models.CharField(max_length=255, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ])
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='inactive', editable=False)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    clients = models.ManyToManyField('Client')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.count >= 0:
            self.status = 'active'
        if self.count == 0:
            self.status = 'inactive'
        super().save(*args, **kwargs)
        if self.status == 'active' and self.time == timezone.now().date():
            self.schedule_next_send()

    def schedule_next_send(self):
        # Method to schedule the next send based on period
        pass

    def check_and_update_status(self):
        if self.count <= 0:
            self.status = 'inactive'
            self.save()

    def get_clients(self):
        return ", ".join([client.name for client in self.clients.all()])

    get_clients.short_description = 'Clients'

    class Meta:
        permissions = [
            ("view_any_mail", "Can view any mail"),  # Разрешение на просмотр любых рассылок
            ("disable_mail", "Can disable mail"),  # Разрешение на отключение рассылок
        ]