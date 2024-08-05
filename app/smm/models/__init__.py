# app/smm/models/__init__.py
__all__ = [
    'Client',
    'Message',
    'Mail',
    'MailAttempt',
]

from app.smm.models.attempt import MailAttempt
from app.smm.models.client import Client
from app.smm.models.mail import Mail
from app.smm.models.message import Message
