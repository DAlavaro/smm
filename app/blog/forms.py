# app/blog/forms.py

from django import forms
from app.blog.models import Blog
from app.smm.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержание'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
