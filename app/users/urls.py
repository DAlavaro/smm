# app/users/urls.py
from django.urls import path

from app.users.views import LoginView, LogoutView, RegisterView, UserUpdateView, genpassword, registration_success

app_name = 'users'


urlpatterns = [

    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', genpassword, name='genpassword'),
    path('registration-success/', registration_success, name='registration_success'),
    # path('signup/', SignUpView.as_view(), name='signup'),
]
