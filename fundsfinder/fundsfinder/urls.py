
# Adicionar as URLs específicas do nosso app api ao projeto
# Arquivo fundsfinder/urls.py
from django.contrib import admin
from django.urls import path, include

# Lista global de rotas (URLs) do projeto fundsfinder
urlpatterns = [
    # Rota base versionada da API (v1):
    # Delega todas as requisições iniciadas com 'api/v1/' para o arquivo api/urls.py.
    # O parâmetro namespace='api' vincula-se ao app_name definido no aplicativo.
    path('api/v1/', include('api.urls', namespace='api')),

    # Rotas de autenticação nativa do Django REST Framework:
    # Habilita os endpoints de login e logout na interface navegável (Browsable API),
    # essenciais para testar views protegidas por permission_classes diretamente no navegador.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Rota padrão do painel administrativo do Django
    path('admin/', admin.site.urls),
]