# app/main/views.py
from django.db.models import Count
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from app.blog.models import Blog
import random

from app.smm.models import Mail, Client


@cache_page(60 * 5)
def home(request):
    # Количество всех рассылок
    total_mailings = Mail.objects.count()

    # Количество активных рассылок
    active_mailings = Mail.objects.filter(status='active').count()

    # Количество уникальных клиентов
    unique_clients = Client.objects.aggregate(count=Count('id', distinct=True))['count']

    # Три случайные статьи из блога
    random_articles = list(Blog.objects.all())
    if len(random_articles) > 3:
        random_articles = random.sample(random_articles, 3)

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
        'random_articles': random_articles,
    }

    return render(request, 'main/home.html', context)
