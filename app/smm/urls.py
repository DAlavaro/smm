# app/smm/urls.py
from django.urls import path

from app.smm.views import (ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView,
                           MessageView, MessageCreateView, MessageUpdateView, MessageDeleteView)

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
]
