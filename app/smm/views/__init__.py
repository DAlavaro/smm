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
]

from app.smm.views.client import ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView
from app.smm.views.message import MessageView, MessageCreateView, MessageUpdateView, MessageDeleteView
