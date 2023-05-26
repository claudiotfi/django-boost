from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, config
from clientes.views import index as clientes_index, connectTo

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('config/', config, name='config'),
    path('clientes/', clientes_index, name='clientes'),
    path('clientes/<str:cliente_alias>/', connectTo, name='connectTo'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
