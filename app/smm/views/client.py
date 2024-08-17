# app/smm/views/client.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.smm.forms import ClientForm
from app.smm.models import Client


class ClientView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('smm:client_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('smm:client_list')

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('smm:client_list')
    template_name = 'smm/client_confirm_delete.html'

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

