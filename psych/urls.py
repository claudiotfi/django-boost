from django.contrib import admin
from django.urls import path
from .views import dashboard, config

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('config/', config, name='config')
]

