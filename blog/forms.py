from django import forms
from .models import *
from django.db import models
from django.utils import timezone

class CadastrarEventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('nome', 'concluido', 'data', 'local', 'endereco', 'cidade', 'estado', 'observacoes')

    def __init__(self, *args, **kwargs):
        super(CadastrarEventoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class' : 'input_grande'})
        self.fields['local'].widget.attrs.update({'class' : 'input_medio'})
        self.fields['endereco'].widget.attrs.update({'class' : 'input_grande'})
        self.fields['cidade'].widget.attrs.update({'class' : 'input_medio'})

class CadastrarPessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('tipoCadastroPessoaFisica', 'tipoCadastroPessoaJuridica', 'tipoPessoaDoador', 'tipoPessoaRecebedor', 'nome', 'cpfCnpj', 'endereco', 'cidade', 'estado', 'telefone1', 'telefone2', 'observacoes')

    def __init__(self, *args, **kwargs):
        super(CadastrarPessoaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class' : 'input_grande'})
        self.fields['endereco'].widget.attrs.update({'class' : 'input_grande'})
        self.fields['cidade'].widget.attrs.update({'class' : 'input_medio'})

class CaixaGeralForm(forms.ModelForm):

    class Meta:
        model = CaixaGeral
        fields = ('pessoa', 'tipoDoacaoDoacao', 'tipoDoacaoRecebimento', 'valor', 'observacoes')

    def __init__(self, *args, **kwargs):
        super(CaixaGeralForm, self).__init__(*args, **kwargs)

class DoacaoForm(forms.ModelForm):

    class Meta:
        model = Doacao
        fields = ('pessoa', 'tipoDoacaoDoacao', 'tipoDoacaoRecebimento', 'data', 'valor', 'observacoes')

    def __init__(self, *args, **kwargs):
        super(DoacaoForm, self).__init__(*args, **kwargs)
