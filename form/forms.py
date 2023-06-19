from django import forms

class Aluno(forms.Form):
    nome = forms.CharField(max_length=250)
    email = forms.EmailField()
    data_nascimento = forms.DateField()