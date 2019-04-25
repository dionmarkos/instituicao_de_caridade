from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/post_list.html', {'posts': posts})

def loginRegistration(request):
    return render(request, 'registration/login.html', {})

def login(request):
    return render(request, 'blog/index.html', {})

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
# MÉTODOS
def validacaoLogin(request, entrada_usuario, entrada_senha):
    try:
        usuario = Usuario.objects.get(nome=entrada_usuario)
        if(usuario.getSenha == entrada_senha):
            return "ok"
    except Exception as usuarioNaoEncontrado:
        usuario = None
