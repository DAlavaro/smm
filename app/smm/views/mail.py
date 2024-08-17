# app/smm/views/mail.py
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView

from app.smm.forms import MailForm
from app.smm.models import Mail, MailAttempt
from django.core.mail import send_mail
from django.contrib.auth.mixins import UserPassesTestMixin


class ManagerPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.groups.filter(name='manager').exists()

    def handle_no_permission(self):
        # Перенаправление на список рассылок, если доступ запрещен
        return redirect('smm:mail_list')


class MailView(LoginRequiredMixin, ListView):
    model = Mail

    def get_queryset(self):
        if self.request.user.has_perm('smm.view_any_mail'):
            return Mail.objects.all()
        return Mail.objects.filter(user=self.request.user)

    def get_template_names(self):
        if self.request.user.groups.filter(name='manager').exists():
            return ['smm/mail_list_manager.html']
        return ['smm/mail_list.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_manager'] = self.request.user.groups.filter(name='manager').exists()
        return context


class MailCreateView(LoginRequiredMixin, ManagerPermissionMixin, CreateView):
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




class MailUpdateView(LoginRequiredMixin, ManagerPermissionMixin, UpdateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('smm:mail_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Mail.objects.filter(user=self.request.user)


class MailDeleteView(LoginRequiredMixin, ManagerPermissionMixin, DeleteView):
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
                # Попытка отправки email
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                )
                # Если успешно, создаем запись с успехом
                MailAttempt.objects.create(
                    mail=mailing,
                    status='success',
                    response=f'Email sent to {client.email}',
                    user=request.user
                )
            except Exception as e:
                # Если неудача, создаем запись с ошибкой
                MailAttempt.objects.create(
                    mail=mailing,
                    status='failure',
                    response=str(e),
                    user=request.user
                )
                messages.error(request, f'Ошибка при отправке письма для {client.email}: {str(e)}')

        messages.success(request, f'Рассылка "{mailing.name}" была успешно отправлена.')
        return redirect('smm:mail_list')


class BlockMailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        # Проверка, чтобы только пользователи с правами менеджера могли блокировать рассылки
        return self.request.user.groups.filter(name='manager').exists()

    def post(self, request, pk):
        mail = get_object_or_404(Mail, pk=pk)
        if mail:
            mail.count = 0
            mail.status = 'inactive'
            mail.save()
            messages.success(request, f'Рассылка "{mail.name}" была успешно заблокирована.')
        else:
            messages.error(request, 'Не удалось найти указанную рассылку.')
        return redirect('smm:mail_list')
