# app/users/management/commands/cmg.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.smm.models import Mail


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Создаем группу "Менеджер"
        manager_group, created = Group.objects.get_or_create(name='manager')

        if created:
            # Получаем контент-тайп для модели Mail
            mail_content_type = ContentType.objects.get_for_model(Mail)

            # Получаем разрешение на просмотр (view) для модели Mail
            view_mail_permission = Permission.objects.get(
                codename='view_mail',
                content_type=mail_content_type
            )

            # Получаем кастомное разрешение на просмотр всех рассылок
            view_any_mail_permission = Permission.objects.get(
                codename='view_any_mail',
                content_type=mail_content_type
            )

            # Назначаем разрешения группе "Менеджер"
            manager_group.permissions.add(view_mail_permission, view_any_mail_permission)

            self.stdout.write(self.style.SUCCESS('Группа "Менеджер" успешно создана и права назначены.'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Менеджер" уже существует.'))
