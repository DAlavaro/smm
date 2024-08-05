# app/smm/views/attempt.py
from django.views.generic import ListView
from app.smm.models import MailAttempt

class MailAttemptListView(ListView):
    model = MailAttempt
    template_name = 'smm/mail_attempt_list.html'
    context_object_name = 'attempts'
