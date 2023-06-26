from django import forms
from .models import Projeto,Curso

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields= '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }
