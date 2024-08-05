# app/smm/urls.py
from django.urls import path

from app.smm.views import (ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView,
                           MessageView, MessageCreateView, MessageUpdateView, MessageDeleteView,
                           MailView, MailCreateView, MailUpdateView, MailDeleteView, SendMailView)
from app.smm.views.attempt import MailAttemptListView

app_name = 'smm'

urlpatterns = [
    path('client/', ClientView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('message/', MessageView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('mail/', MailView.as_view(), name='mail_list'),
    path('mail/create/', MailCreateView.as_view(), name='mail_create'),
    path('mail/<int:pk>/update/', MailUpdateView.as_view(), name='mail_update'),
    path('mail/<int:pk>/delete/', MailDeleteView.as_view(), name='mail_delete'),
    path('mail/<int:pk>/send/', SendMailView.as_view(), name='send_mail'),

    path('attempt/', MailAttemptListView.as_view(), name='mail_attempt_list'),
]
