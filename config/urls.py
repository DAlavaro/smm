# config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.main.urls'), name='main'),
    path('smm/', include('app.smm.urls'), name='smm'),
    path('users/', include('app.users.urls'), name='users'),
    path('blog/', include('app.blog.urls'), name='blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)