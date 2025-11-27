from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class Login(View):

    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("listar-veiculos")
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        usuario = request.POST.get('email', None)
        senha = request.POST.get('password', None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("listar-veiculos")
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo!'})
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário e senha inválidos!'})

class Logout(View):
    def post(self, request):
        logout(request)
        return redirect('/login/')

class LoginApi(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user= serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id, 'username': user.username, 'email': user.email, 'token': token.key})

class Registrar(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data.get('password1')
            user = form.save()
            user = authenticate(request, username=user.get_username(), password=raw_password)
            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                contexto = {
                    'token': token.key,
                    'api_url': '/api/listar/',  
                    'mensagem': 'Conta criada e logada com sucesso.',
                }
                return render(request, 'autenticacao.html', contexto)
        return render(request, 'registro.html', {'form': form})


