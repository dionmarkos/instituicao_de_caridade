from django.shortcuts import render
from django.utils import timezone
from .forms import *

def servicos(request):
    return render(request, 'blog/servicos.html', {})

def cadastrar_pessoa(request):
    if request.method == "POST":
        form = CadastrarPessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.autor = request.user
            pessoa.dataDeCadastro = timezone.now()
            pessoa.save()
    else:
        form = CadastrarPessoaForm()
    return render(request, 'blog/cadastrar_pessoa.html', {'form': form})

def cadastrar_evento(request):
    if request.method == "POST":
        form = CadastrarEventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.autor = request.user
            evento.dataDeCadastro = timezone.now()
            evento.save()
    else:
        form = CadastrarEventoForm()
    return render(request, 'blog/cadastrar_evento.html', {'form': form})

def caixa_geral(request):
    if request.method == "POST":
        form = CaixaGeralForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.autor = request.user
            transacao.save()
    else:
        form = CaixaGeralForm()
    return render(request, 'blog/caixa_geral.html', {'form': form})

def consultas(request):
    return render(request, 'blog/consultas.html', {})

def doacoes(request):
    if request.method == "POST":
        form = DoacaoForm(request.POST)
        if form.is_valid():
            doacao = form.save(commit=False)
            doacao.autor = request.user
            doacao.save()
    else:
        form = DoacaoForm()
    return render(request, 'blog/doacoes.html', {'form': form})
