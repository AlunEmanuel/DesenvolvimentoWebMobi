from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns= [
    path('', login_required(ListarVeiculos.as_view(),login_url='login'), name='listar-veiculos'),
    path('cadastrar-veiculos/', login_required(CadastrarVeiculos.as_view(),login_url='login'), name='cadastrar-veiculos'),
]