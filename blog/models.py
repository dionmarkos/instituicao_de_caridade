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
    tipo_cadastro_pessoa_fisica = models.BooleanField(default=True)
    tipo_cadastro_pessoa_juridica = models.BooleanField(default=False)
    tipo_pessoa_doador = models.BooleanField(default=True)
    tipo_pessoa_recebedor = models.BooleanField(default=False)
    nome = models.TextField()
    cpf_cnpj = models.CharField(max_length=14)
    endereco = models.TextField()
    cidade = models.TextField()
    estado = models.TextField()
    telefone1 = models.CharField(max_length=10)
    telefone2 = models.CharField(max_length=10)
    observacoes = models.TextField()



class Evento(models.Model):
    nome = models.TextField()
    data = models.DateTimeField()
    boolean_concluido = models.BooleanField(default=False)
    local = models.TextField()
    endereco = models.TextField()
    cidade = models.TextField()
    estado = models.TextField()
    observacoes = models.TextField()

class Doacao(models.Model):
    pessoa = models.ForeignKey('Pessoa',on_delete=models.CASCADE)
    tipo_doacao_doacao = models.BooleanField(default=True)
    tipo_doacao_recebimento = models.BooleanField(default=False)
    data = models.DateTimeField()
    valor = models.TextField()
    observacoes = models.TextField()

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
    pessoa = Pessoa()
    evento = Evento()
    doacoes = Doacao()
    transacao = CaixaGeral()
    usuario = Usuario()
