from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View, UpdateView, DeleteView

from veiculos.serializers import VeiculoSerializer
from .models import Veiculo
from .forms import VeiculoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

class Login(View):
    def get(self, request):
        contexto = {}
        if request.user.is_authenticated:
            return redirect("/veiculos")
        else:
            return render(request, 'autenticacao.html', contexto)
        
class ListarVeiculos(LoginRequiredMixin,ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculos/listar.html'

class CadastrarVeiculos(LoginRequiredMixin,CreateView):
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('listar-veiculos') 

class EditarVeiculos(LoginRequiredMixin,UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('listar-veiculos') 

class ExcluirVeiculos (LoginRequiredMixin,DeleteView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculos/excluir.html' 
    success_url = reverse_lazy('listar-veiculos')

class APINFOveiculos(ListAPIView):
    serializer_class = VeiculoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Veiculo.objects.all()