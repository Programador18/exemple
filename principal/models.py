import datetime
from django.db import models
from django.utils import timezone

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	ultima_postagem = models.DateTimeField('ultima_postagem')

class Postagem(models.Model):
	pessoa = models.ForeignKey(Pessoa, 
on_delete=models.CASCADE)
	texto = models.CharField(max_length=500)
	curtidas = models.IntegerField(default=0)

# Create your models here.
