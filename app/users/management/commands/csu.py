# app/users/management/commands/csu.py
from django.core.management import BaseCommand

from app.users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.all().create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='Adminov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('admin')
        user.save()
