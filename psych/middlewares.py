from .utils import get_config

class ConfigMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.config = get_config()  # Obtém a configuração global

    def __call__(self, request):
        # Adiciona o contexto global à requisição
        request.config = self.config
        return self.get_response(request)
