from django.shortcuts import render
from .models import Projeto
from .forms import ProjetoForm

def cadastro_projeto(request):

    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProjetoForm()
            #nome = form.cleaned_data['nome']
            #descricao = form.cleaned_data['descricao']
            #data_criacao = form.cleaned_data['data_criacao']
            #salvando o aluno no banco.
            #print("Nome: {} - Descrição: {} - Data de criação: {}".format(nome,descricao,data_criacao))
            #Projeto.objects.create(nome=nome, descricao=descricao,data_criacao=data_criacao)
    else:
        print("->>>> entrou primeiro aqui")
        form = ProjetoForm()

    return render(request, 'projeto/form_projeto.html', {'form': form})