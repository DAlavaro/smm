# app/users/forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from app.smm.forms import StyleFormMixin
from app.users.models import User


class CustomAuthenticationForm(StyleFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Электронная почта'


class UserRegisterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'avatar']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
