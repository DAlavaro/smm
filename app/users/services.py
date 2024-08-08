# app/users/services.py
from django.core.mail import send_mail
from django.conf import settings
from app.users.models import User


def generate_and_send_password(user):
    """Generates a random password for the user and sends it via email."""
    new_password = User.objects.make_random_password()
    user.set_password(new_password)
    user.save()
    send_mail(
        subject='Ваш новый пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )
