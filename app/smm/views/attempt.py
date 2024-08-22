from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from app.smm.models import MailAttempt

class MailAttemptListView(LoginRequiredMixin, ListView):
    model = MailAttempt
    template_name = 'smm/mail_attempt_list.html'
    context_object_name = 'attempts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return MailAttempt.objects.filter(user=self.request.user)
        else:
            return MailAttempt.objects.none()  # Возвращаем пустой QuerySet для анонимных пользователей
