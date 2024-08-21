# app/users/management/commands/cmg.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.smm.models import Mail
from app.blog.models import Blog  # Импортируем модель Blog

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Создаем группу "manager"
        manager_group, created_manager = Group.objects.get_or_create(name='manager')

        if created_manager:
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

            # Назначаем разрешения группе "manager"
            manager_group.permissions.add(view_mail_permission, view_any_mail_permission)

            self.stdout.write(self.style.SUCCESS('Группа "manager" успешно создана и права назначены.'))
        else:
            self.stdout.write(self.style.WARNING('Группа "manager" уже существует.'))

        # Создаем группу "content_manager"
        content_manager_group, created_content_manager = Group.objects.get_or_create(name='content_manager')

        if created_content_manager:
            # Получаем контент-тайп для модели Blog
            blog_content_type = ContentType.objects.get_for_model(Blog)

            # Получаем разрешения для модели Blog
            add_blog_permission = Permission.objects.get(
                codename='add_blog',
                content_type=blog_content_type
            )
            change_blog_permission = Permission.objects.get(
                codename='change_blog',
                content_type=blog_content_type
            )
            delete_blog_permission = Permission.objects.get(
                codename='delete_blog',
                content_type=blog_content_type
            )

            # Назначаем разрешения группе "content_manager"
            content_manager_group.permissions.add(
                add_blog_permission,
                change_blog_permission,
                delete_blog_permission
            )

            self.stdout.write(self.style.SUCCESS('Группа "content_manager" успешно создана и права назначены.'))
        else:
            self.stdout.write(self.style.WARNING('Группа "content_manager" уже существует.'))
