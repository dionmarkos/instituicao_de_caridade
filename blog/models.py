# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE) #link para outro modelo
    titulo = models.CharField(max_length=200) #caracteres limitados
    texto = models.TextField() #string sem limites
    data_criacao = models.DateTimeField(default=timezone.now) #formato para datas
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Pessoa(models.Model):
    tipoCadastroPessoaFisica = models.BooleanField(default=True)
    tipoCadastroPessoaJuridica = models.BooleanField(default=False)
    tipoPessoaDoador = models.BooleanField(default=True)
    tipoPessoaRecebedor = models.BooleanField(default=False)
    nome = models.TextField()
    cpfCnpj = models.CharField(max_length=14)
    endereco = models.TextField()
    cidade = models.TextField()
    estado = models.TextField()
    telefone1 = models.CharField(max_length=10)
    telefone2 = models.CharField(max_length=10)
    observacoes = models.TextField()
    dataDeCadastro = models.DateTimeField()
# CONSTRUTOR
    def __init__(self, tipoCadastroPessoaFisica, tipoCadastroPessoaJuridica, tipoPessoaDoador, tipoPessoaRecebedor, nome, cpfCnpj, endereco, cidade, estado, telefone1, telefone2, observacoes):
        self.tipoCadastroPessoaFisica = tipoCadastroPessoaFisica
        self.tipoCadastroPessoaJuridica = tipoCadastroPessoaJuridica
        self.tipoPessoaDoador = tipoPessoaDoador
        self.tipoPessoaRecebedor = tipoPessoaRecebedor
        self.nome = nome
        self.cpfCnpj = cpfCnpj
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.telefone1 = telefone1
        self.telefone2 = telefone2
        self.observacoes = observacoes
        self.dataDeCadastro = timezone.now()
        self.save()
# GETS
    def getTipoCadastroPessoaFisica(self):
        return self.tipoCadastroPessoaFisica

    def getTipoCadastroPessoaJuridica(self):
        return self.tipoCadastroPessoaJuridica

    def getTipoPessoaDoador(self):
        return self.tipoPessoaDoador

    def getTipoPessoaRecebedor(self):
        return self.tipoPessoaRecebedor

    def getNome(self):
        return self.nome

    def getCpfCnpj(self):
        return self.cpfCnpj

    def getEndereco(self):
        return self.endereco

    def getCidade(self):
        return self.cidade

    def getEstado(self):
        return self.estado

    def getTelefone1(self):
        return self.telefone1

    def getTelefone2(self):
        return self.telefone2

    def getObservacoes(self):
        return self.observacoes

    def getDataDeCadastro(self):
        return self.dataDeCadastro
# SETS
    def setTipoCadastroPessoaFisica(self, tipoCadastroPessoaFisica):
        self.tipoCadastroPessoaFisica = tipoCadastroPessoaFisica

    def setTipoCadastroPessoaJuridica(self, tipoCadastroPessoaJuridica):
        self.tipoCadastroPessoaJuridica = tipoCadastroPessoaJuridica

    def setTipoPessoaDoador(self, tipoPessoaDoador):
        self.tipoPessoaDoador = tipoPessoaDoador

    def setTipoPessoaRecebedor(self, tipoPessoaRecebedor):
        self.tipoPessoaRecebedor = tipoPessoaRecebedor

    def setNome(self, nome):
        self.nome = nome

    def setCpfCnpj(self, cpfCnpj):
        self.cpfCnpj = cpfCnpj

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setCidade(self, cidade):
        self.cidade = cidade

    def setEstado(self, estado):
        self.estado = estado

    def setTelefone1(self, telefone1):
        self.telefone1 = telefone1

    def setTelefone2(self, telefone2):
        self.telefone2 = telefone2

    def setObservacoes(self, observacoes):
        self.observacoes = observacoes
# *******FIM DA CLASSE PESSOA********
class Evento(models.Model):
    nome = models.TextField()
    data = models.DateTimeField()
    booleanConcluido = models.BooleanField(default=False)
    local = models.TextField()
    endereco = models.TextField()
    cidade = models.TextField()
    estado = models.TextField()
    observacoes = models.TextField()
    dataDeCadastro = models.DateTimeField()
# CONSTRUTOR
    def __init__(self, nome, data, booleanConcluido, local, endereco, cidade, estado, observacoes):
        self.nome = nome
        self.data = data
        self.booleanConcluido = booleanConcluido
        self.local = local
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.observacoes = observacoes
        self.dataDeCadastro = timezone.now()
# GETS
    def getNome(self):
        return self.nome

    def getData(self):
        return self.data

    def getBooleanConcluido(self):
        return self.booleanConcluido

    def getLocal(self):
        return self.local

    def getEndereco(self):
        return self.endereco

    def getCidade(self):
        return self.cidade

    def getEstado(self):
        return self.estado

    def getObservacoes(self):
        return self.observacoes

    def getDataDeCadastro(self):
        return self.dataDeCadastro
# SETS
    def setNome(self, nome):
        self.nome = nome

    def setData(self, data):
        self.data = data

    def setBooleanConcluido(self, booleanConcluido):
        self.booleanConcluido = booleanConcluido

    def setLocal(self, local):
        self.local = local

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setCidade(self, cidade):
        self.cidade = cidade

    def setEstado(self, estado):
        self.estado = estado

    def setObservacoes(self, observacoes):
        self.observacoes = observacoes
# *******FIM DA CLASSE EVENTO********
class Doacao(models.Model):
    pessoa = models.ForeignKey('Pessoa',on_delete=models.CASCADE)
    tipo_doacao_doacao = models.BooleanField(default=True)
    tipo_doacao_recebimento = models.BooleanField(default=False)
    data = models.DateTimeField()
    valor = models.TextField()
    observacoes = models.TextField()
# CONSTRUTOR


class CaixaGeral(models.Model):
    pessoa = models.ForeignKey('Pessoa',on_delete=models.CASCADE)
    tipo_doacao_doacao = models.BooleanField(default=True)
    tipo_doacao_recebimento = models.BooleanField(default=False)
    data = models.DateTimeField()
    valor = models.TextField()
    observacoes = models.TextField()

class Usuario(models.Model):
    tipo_usuario_basico = models.BooleanField(default=True)
    tipo_usuario_admninistrador = models.BooleanField(default=False)
    nome = models.TextField()
    usuario = models.CharField(max_length=18)
    senha = models.TextField()
    observacoes = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

class Consulta(models.Model):
    pessoa = models.ForeignKey('Pessoa',on_delete=models.CASCADE)
    evento = models.ForeignKey('Evento',on_delete=models.CASCADE)
    doacoes = models.ForeignKey('Doacao',on_delete=models.CASCADE)
    transacao = models.ForeignKey('CaixaGeral',on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
