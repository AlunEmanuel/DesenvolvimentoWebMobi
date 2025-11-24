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
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import UserCreationForm

class Login(View):
    def get(self, request):
        contexto = {}
        if request.user.is_authenticated:
            return redirect("/veiculos")
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        """
        Autentica usando o campo 'email' do form (pode ser email ou username),
        faz login de sessão e retorna o token e link da API no mesmo template.
        """
        email_or_username = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Tenta autenticar diretamente como username
        user = authenticate(request, username=email_or_username, password=password)

        if user is None:
            # Se falhar, tenta encontrar pelo email e autenticar com o username real
            User = get_user_model()
            try:
                u = User.objects.get(email=email_or_username)
                user = authenticate(request, username=u.get_username(), password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            contexto = {
                'token': token.key,
                'api_url': '/api/listar/',  
            }
            return render(request, 'autenticacao.html', contexto)
        else:
            contexto = {'error': 'Credenciais inválidas.'}
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
