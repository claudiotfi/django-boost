import logging
from .utils import get_config

class ConfigMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.config = get_config()  # Obtém a configuração global

    def __call__(self, request):
        # Adiciona o contexto global à requisição
        request.config = self.config
        return self.get_response(request)
    
class ContextProcessorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lógica do contexto do processador aqui
        request.debug = 'texto estático'
        
        # Log da variável request.debug
        logging.debug(f"Valor de request.debug: {request.debug}")
        
        return self.get_response(request)

