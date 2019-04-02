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