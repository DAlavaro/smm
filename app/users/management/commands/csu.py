# app/users/management/commands/csu.py
from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from app.users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):

        # Создание или обновление суперпользователя
        admin_user, created = User.objects.get_or_create(
            email='admin@sky.pro',
            defaults={
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
            }
        )
        if created:
            admin_user.set_password('admin')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Суперпользователь создан.'))
        else:
            self.stdout.write(self.style.WARNING('Суперпользователь уже существует.'))

        # Создание или обновление пользователя-менеджера
        manager_user, created = User.objects.get_or_create(
            email='manager@sky.pro',
            defaults={
                'first_name': 'Manager',
                'last_name': 'Managerov',
                'is_superuser': False,
                'is_staff': True,
                'is_active': True,
            }
        )
        if created:
            manager_user.set_password('manager')
            manager_user.save()

            # Назначение прав менеджера
            try:
                manager_group = Group.objects.get(name='manager')
                manager_user.groups.add(manager_group)
                self.stdout.write(self.style.SUCCESS('Пользователь-менеджер создан и добавлен в группу "manager".'))
            except Group.DoesNotExist:
                self.stdout.write(self.style.ERROR('Группа "manager" не существует. Пожалуйста, создайте её сначала.'))
        else:
            self.stdout.write(self.style.WARNING('Пользователь-менеджер уже существует.'))

        # Создание или обновление пользователя-контент менеджера
        content_manager_user, created = User.objects.get_or_create(
            email='content_manager@sky.pro',
            defaults={
                'first_name': 'Content',
                'last_name': 'Managerov',
                'is_superuser': False,
                'is_staff': True,
                'is_active': True,
            }
        )
        if created:
            content_manager_user.set_password('content_manager')
            content_manager_user.save()

            # Назначение прав контент-менеджера
            try:
                content_manager_group = Group.objects.get(name='content_manager')
                content_manager_user.groups.add(content_manager_group)
                self.stdout.write(self.style.SUCCESS('Пользователь-контент менеджер создан и добавлен в группу "content_manager".'))
            except Group.DoesNotExist:
                self.stdout.write(self.style.ERROR('Группа "content_manager" не существует. Пожалуйста, создайте её сначала.'))
        else:
            self.stdout.write(self.style.WARNING('Пользователь-контент менеджер уже существует.'))
