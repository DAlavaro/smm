# app/smm/views/client.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.smm.forms import ClientForm
from app.smm.models import Client


class ClientView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('smm:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('smm:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('smm:client_list')
    template_name = 'smm/client_confirm_delete.html'
