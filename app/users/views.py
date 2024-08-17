# app/users/views.py
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from app.users.forms import CustomAuthenticationForm, UserRegisterForm, UserForm
from app.users.models import User
from app.users.services import generate_and_send_password


class LoginView(BaseLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.is_blocked:
            return HttpResponse("Вы заблокированы. Свяжитесь с администрацией сайта.", status=403)
        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    template_name = 'users/logout.html'


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        generate_and_send_password(self.object)
        return redirect('users:registration_success')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        generate_and_send_password(self.object)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


def genpassword(request):
    """Random password generator"""
    generate_and_send_password(request.user)
    return redirect(reverse('main:home'))


def registration_success(request):
    return render(request, 'users/registration_success.html')


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return User.objects.all().order_by('email')

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)
        user.is_blocked = not user.is_blocked
        user.save()
        return redirect('users:user_list')
