# app/smm/admin.py
from django.contrib import admin
from app.smm.models import Client, Message, Mail, MailAttempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'count', 'period', 'message', 'get_clients')
