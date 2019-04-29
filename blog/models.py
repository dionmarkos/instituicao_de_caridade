# Create your models here.
from django.db import models
from django.utils import timezone

# class Post(models.Model):
#     autor = models.ForeignKey('auth.User', on_delete=models.CASCADE) #link para outro modelo
#     titulo = models.CharField(max_length=200) #caracteres limitados
#     # texto = models.TextField() #string sem limites
#     data_criacao = models.DateTimeField(default=timezone.now) #formato para datas
#     data_publicacao = models.DateTimeField(blank=True, null=True)
#
#     def publicar(self):
#         self.data_publicacao = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.titulo

class Pessoa(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    tipoCadastroPessoaFisica = models.BooleanField(default=True)
    tipoCadastroPessoaJuridica = models.BooleanField(default=False)
    tipoPessoaDoador = models.BooleanField(default=True)
    tipoPessoaRecebedor = models.BooleanField(default=False)
    nome = models.CharField(max_length=50)
    cpfCnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=20)
    telefone1 = models.CharField(max_length=14)
    telefone2 = models.CharField(max_length=14)
    observacoes = models.TextField()
    dataDeCadastro = models.DateTimeField()

class Evento(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50)
    data = models.DateTimeField(default=timezone.now)
    concluido = models.BooleanField(default=False)
    local = models.CharField(max_length=80)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=20)
    observacoes = models.TextField()
    dataDeCadastro = models.DateTimeField()

class Doacao(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)
    tipoDoacaoDoacao = models.BooleanField(default=True)
    tipoDoacaoRecebimento = models.BooleanField(default=False)
    data = models.DateTimeField()
    valor = models.CharField(max_length=20)
    observacoes = models.TextField()

class CaixaGeral(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)
    tipoDoacaoDoacao = models.BooleanField(default=True)
    tipoDoacaoRecebimento = models.BooleanField(default=False)
    valor = models.CharField(max_length=20)
    observacoes = models.TextField()

class Consulta(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    pessoa = models.ForeignKey('Pessoa',on_delete=models.DO_NOTHING)
    evento = models.ForeignKey('Evento',on_delete=models.DO_NOTHING)
    doacoes = models.ForeignKey('Doacao',on_delete=models.DO_NOTHING)
    transacao = models.ForeignKey('CaixaGeral',on_delete=models.DO_NOTHING)
