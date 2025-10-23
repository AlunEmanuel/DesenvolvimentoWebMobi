from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListarVeiculos, CadastrarVeiculos, EditarVeiculos, ExcluirVeiculos

urlpatterns = [
    path('', login_required(ListarVeiculos.as_view()), name='listar-veiculos'),
    path('novo/', login_required(CadastrarVeiculos.as_view()), name='cadastrar-veiculos'),
    path('editar/<int:pk>/', login_required(EditarVeiculos.as_view()), name='editar-veiculos'),
    path('excluir/<int:pk>/', login_required(ExcluirVeiculos.as_view()), name='excluir-veiculos'),
]