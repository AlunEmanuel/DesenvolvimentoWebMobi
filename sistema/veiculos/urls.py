from django.urls import path
from . import views

urlpatterns = [
    # raiz do app -> listagem (raiz do site se include('veiculos.urls') estiver em projeto)
    path('', views.ListarVeiculos.as_view(), name='listar-veiculos'),

    # rotas de CRUD usadas nos templates
    path('cadastrar/', views.CadastrarVeiculos.as_view(), name='cadastrar-veiculos'),
    path('editar/<int:pk>/', views.EditarVeiculos.as_view(), name='editar-veiculos'),
    path('excluir/<int:pk>/', views.ExcluirVeiculos.as_view(), name='excluir-veiculos'),

    # API protegida (nome simples)
    path('api/listar/', views.APINFOveiculos.as_view(), name='api-listar'),
]