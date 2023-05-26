from django.shortcuts import render
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'index.html', context)


