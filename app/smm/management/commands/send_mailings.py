# app/smm/management/commands/send_mailings.py

import logging
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

from app.smm.cron import my_job
from app.smm.models import Mail
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Отправляет рассылки клиентам'

    def handle(self, *args, **kwargs):
        my_job()

        # today = timezone.now().date()
        # mails = Mail.objects.filter(status='active', time__lte=today)
        #
        # for mail in mails:
        #     clients = mail.clients.all()
        #     message = mail.message.text
        #     subject = mail.message.name
        #
        #     for client in clients:
        #         try:
        #             send_mail(
        #                 subject=subject,
        #                 message=message,
        #                 from_email=settings.EMAIL_HOST_USER,
        #                 recipient_list=[client.email],
        #             )
        #             logger.info(f"Email sent to {client.email} for mailing {mail.name}")
        #         except Exception as e:
        #             logger.error(f"Error sending email to {client.email} for mailing {mail.name}: {e}")
        #
        #     mail.count -= 1
        #     if mail.count <= 0:
        #         mail.status = 'inactive'
        #     else:
        #         if mail.period == 'daily':
        #             mail.time += timedelta(days=1)
        #         elif mail.period == 'weekly':
        #             mail.time += timedelta(weeks=1)
        #         elif mail.period == 'monthly':
        #             mail.time += timedelta(weeks=4)
        #
        #     mail.save()
        #     logger.info(f"Processed mailing: {mail.name}, remaining count: {mail.count}")
