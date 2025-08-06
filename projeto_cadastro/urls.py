
from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.prin,name='prin'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_pessoas')
]
