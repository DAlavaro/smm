# app/smm/forms.py
from django.utils import timezone

from django import forms
from app.smm.models import Client, Message, Mail


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'comment']

class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'text']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


class MailForm(StyleFormMixin, forms.ModelForm):
    time = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Дата начала отправки рассылки'
    )

    clients = forms.ModelMultipleChoiceField(
        queryset=Client.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Клиенты'
    )

    message = forms.ModelChoiceField(
        queryset=Message.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label='Сообщение'
    )

    class Meta:
        model = Mail
        fields = ['name', 'time', 'count', 'period', 'message', 'clients']
        widgets = {
            'period': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['clients'].queryset = Client.objects.filter(user=user)
            self.fields['message'].queryset = Message.objects.filter(user=user)

            if self.instance.pk:
                self.fields['clients'].initial = self.instance.clients.all()
                self.fields['message'].initial = self.instance.message

    def clean_time(self):
        time = self.cleaned_data['time']
        if time < timezone.now().date():
            raise forms.ValidationError("Дата начала отправки не может быть в прошлом.")
        return time
