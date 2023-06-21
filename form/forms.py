from django import forms
from .models import Aluno

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=250)
    email = forms.EmailField()
    data_nascimento = forms.DateField()