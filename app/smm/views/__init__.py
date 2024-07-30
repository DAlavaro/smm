# app/smm/views/__init__.py
__all__ = [
    'ClientView',
    'ClientCreateView',
    'ClientUpdateView',
    'ClientDeleteView',

    'MessageView',
    'MessageCreateView',
    'MessageUpdateView',
    'MessageDeleteView',

    'MailView',
    'MailCreateView',
    'MailUpdateView',
    'MailDeleteView',
    'SendMailView',
]

from app.smm.views.client import ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView
from app.smm.views.mail import MailView, MailCreateView, MailUpdateView, MailDeleteView, SendMailView
from app.smm.views.message import MessageView, MessageCreateView, MessageUpdateView, MessageDeleteView
