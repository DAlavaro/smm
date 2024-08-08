# app/smm/views/mail.py
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from app.smm.forms import MailForm
from app.smm.models import Mail
from django.core.mail import send_mail


class MailView(LoginRequiredMixin, ListView):
    model = Mail

    def get_queryset(self):
        return Mail.objects.filter(user=self.request.user)


class MailCreateView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('smm:mail_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailUpdateView(LoginRequiredMixin, UpdateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('smm:mail_list')

    def get_queryset(self):
        return Mail.objects.filter(user=self.request.user)


class MailDeleteView(LoginRequiredMixin,DeleteView):
    model = Mail
    success_url = reverse_lazy('smm:mail_list')
    template_name = 'smm/mail_confirm_delete.html'

    def get_queryset(self):
        return Mail.objects.filter(user=self.request.user)


class SendMailView(LoginRequiredMixin, View):
    def post(self, request, pk):
        mailing = get_object_or_404(Mail, pk=pk, user=request.user)
        clients = mailing.clients.all()
        message = mailing.message.text
        subject = mailing.message.name

        for client in clients:
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                )
            except Exception as e:
                messages.error(request, f'Ошибка при отправке письма для {client.email}: {str(e)}')

        messages.success(request, f'Рассылка "{mailing.name}" была успешно отправлена.')
        return redirect('smm:mail_list')
