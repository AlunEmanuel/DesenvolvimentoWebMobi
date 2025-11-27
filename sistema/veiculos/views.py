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
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token

class Login(View):
    def get(self, request):
        contexto = {}
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        email_or_username = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=email_or_username, password=password)

        if user is None:
            User = get_user_model()
            try:
                u = User.objects.get(email=email_or_username)
                user = authenticate(request, username=u.get_username(), password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            contexto = {'error': 'Credenciais inválidas.'}
            return render(request, 'autenticacao.html', contexto)

class ListarVeiculos(LoginRequiredMixin, ListView):
    login_url = '/login/'               
    redirect_field_name = 'next'
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculos/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_authenticated'] = self.request.user.is_authenticated
        if self.request.user.is_authenticated:
            context['api_url'] = '/api/listar/'
            token, _ = Token.objects.get_or_create(user=self.request.user)
            context['token'] = token.key
            host = self.request.get_host()
            context['api_cmd_header'] = f"curl -H \"Authorization: Token {token.key}\" http://{host}{context['api_url']}"
        return context

class CadastrarVeiculos(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('listar-veiculos') 

class EditarVeiculos(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('listar-veiculos') 

class ExcluirVeiculos (LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'next'
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
