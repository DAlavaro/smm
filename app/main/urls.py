from django.urls import path
from app.main.views import home

app_name = 'main'


urlpatterns = [
    path('', home, name='home'),
]
