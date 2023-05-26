from django.shortcuts import redirect
from django.contrib import messages
from clientes.models import Cliente
import mysql.connector
from django.core import serializers

class ClienteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'cliente' not in request.session:
            # Redirecionar para /clientes se request.session['cliente'] não existir
            return redirect('clientes')

        cliente_dict = request.session['cliente']
        cliente_alias = cliente_dict['alias']

        try:
            # Obter o cliente com base no alias
            cliente = Cliente.objects.get(alias=cliente_alias)

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
                request._messages._queued_messages = []
                messages.success(request, f"Conectado ao banco de dados: {cliente.db_database}")

            # Fechar conexão
            conn.close()

        except Cliente.DoesNotExist:
            # Tratar cliente não encontrado
            messages.error(request, "Cliente não localizado")
            return redirect('clientes')

        except mysql.connector.Error as e:
            # Tratar erros de conexão
            messages.error(request, f"Erro ao conectar ao banco de dados: {e}")
            return redirect('clientes')

        response = self.get_response(request)
        return response
