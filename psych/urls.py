from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, config

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('config/', config, name='config')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

