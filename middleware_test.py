import os
import django
from django.http import HttpRequest, HttpResponse
from django.contrib.sessions.middleware import SessionMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psych.settings')
django.setup()

from middleware.cliente_middleware import ClienteMiddleware

def test_middleware():
    middleware = ClienteMiddleware(get_response=None)  # Passando None como get_response, pois não é necessário para o teste
    request = HttpRequest()
    response = HttpResponse()
    
    # Adicionar o middleware de sessão ao objeto HttpRequest
    SessionMiddleware(lambda req: response).process_request(request)
    
    response = middleware(request)
    # Faça algo com a resposta, se necessário
    return response

# Testar o middleware
test_middleware()
