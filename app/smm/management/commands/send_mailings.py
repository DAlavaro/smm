# app/smm/management/commands/send_mailings.py

import logging
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from app.smm.models import Mail, MailAttempt
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Отправляет рассылки клиентам'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        mails = Mail.objects.filter(status='active', time__lte=today)

        for mail in mails:
            # Создание записи о попытке рассылки
            attempt = MailAttempt(mail=mail)
            try:
                clients = mail.clients.all()
                message = mail.message.text
                subject = mail.message.name
                success = True
                response = ''

                for client in clients:
                    try:
                        send_mail(
                            subject=subject,
                            message=message,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[client.email],
                        )
                        logger.info(f"Email sent to {client.email} for mailing {mail.name}")
                    except Exception as e:
                        success = False
                        response += f"Error sending email to {client.email}: {str(e)}\n"
                        logger.error(f"Error sending email to {client.email} for mailing {mail.name}: {e}")

                if success:
                    attempt.status = 'success'
                else:
                    attempt.status = 'failure'
                    attempt.response = response

                attempt.save()

                # Обновление статуса и времени следующей рассылки
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
                logger.info(f"Processed mailing: {mail.name}, remaining count: {mail.count}")

            except Exception as e:
                # Если ошибка в процессе рассылки, сохраняем её в статистике
                attempt.status = 'failure'
                attempt.response = str(e)
                attempt.save()
                logger.error(f"Failed to process mailing {mail.name}: {e}")