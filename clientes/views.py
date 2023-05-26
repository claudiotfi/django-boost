from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente
import mysql.connector
from django.core import serializers

def index(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'index.html', context)

def connectTo(request, cliente_alias):
    cliente = Cliente.objects.get(alias=cliente_alias)

    if cliente == '':
        messages.error(request, "Cliente não localizado")
        return redirect('clientes')

    try:
        # Estabelecer conexão com o banco de dados do cliente
        conn = mysql.connector.connect(
            host=cliente.db_host,
            port=cliente.db_port,
            user=cliente.db_username,
            password=cliente.db_password,
            database=cliente.db_database,
        )

        if conn.is_connected():

            # Converter o objeto Cliente em um dicionário
            cliente_data = serializers.serialize('python', [cliente])[0]
            cliente_dict = cliente_data['fields']

            # Armazenar o dicionário do cliente na sessão
            request.session['cliente'] = cliente_dict

            # Exibir mensagem com o nome do banco conectado
            #messages.success(request, f"Conectado ao banco de dados: {cliente.db_database}")
            request._messages._queued_messages = []
            
        # Fechar conexão
        conn.close()

    except mysql.connector.Error as e:
        # Tratar erros de conexão
        messages.error(request, f"Erro ao conectar ao banco de dados: {e}")

    return redirect('/')
