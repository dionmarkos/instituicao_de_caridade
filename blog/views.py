from django.shortcuts import render
from django.utils import timezone
from .models import Post

def servicos(request):
    return render(request, 'blog/servicos.html', {})

def cadastrar_pessoa(request):
    return render(request, 'blog/cadastrar_pessoa.html', {})

def cadastrar_evento(request):
    return render(request, 'blog/cadastrar_evento.html', {})

def cadastrar_usuario(request):
    return render(request, 'blog/cadastrar_usuario.html', {})

def caixa_geral(request):
    return render(request, 'blog/caixa_geral.html', {})

def consultas(request):
    return render(request, 'blog/consultas.html', {})

def doacoes(request):
    return render(request, 'blog/doacoes.html', {})
