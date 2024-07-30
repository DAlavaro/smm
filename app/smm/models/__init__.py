# app/smm/models/__init__.py
__all__ = [
    'Client',
    'Message',
    'Mail',
]

from app.smm.models.client import Client
from app.smm.models.mail import Mail
from app.smm.models.message import Message
