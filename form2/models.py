from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=250, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    data_criacao = models.DateField(verbose_name='Data de criação')