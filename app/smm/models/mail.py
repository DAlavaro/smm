# app/smm/models.py
from django.db import models
from django.utils import timezone


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