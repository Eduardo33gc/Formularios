from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    data_nascimento = models.DateField()