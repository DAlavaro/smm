# app/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Электронная почта')

    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='Аватар')

    is_blocked = models.BooleanField(default=False, verbose_name='Заблокирован')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
