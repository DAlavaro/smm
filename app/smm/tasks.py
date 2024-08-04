# app/smm/tasks.py
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from app.smm.models import Mail


@shared_task
def send_mailings():
    today = timezone.now().date()
    mails = Mail.objects.filter(status='active', time__lte=today)

    for mail in mails:
        clients = mail.clients.all()
        message = mail.message.text
        subject = mail.message.name

        for client in clients:
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                )
                print(f"Email sent to {client.email} for mailing {mail.name}")
            except Exception as e:
                print(f"Error sending email to {client.email} for mailing {mail.name}: {e}")

        mail.count -= 1
        if mail.count <= 0:
            mail.status = 'inactive'
        else:
            if mail.period == 'daily':
                mail.time += timedelta(days=1)
            elif mail.period == 'weekly':
                mail.time += timedelta(weeks=1)
            elif mail.period == 'monthly':
                mail.time += timedelta(weeks=4)

        mail.save()
        print(f"Processed mailing: {mail.name}, remaining count: {mail.count}")
