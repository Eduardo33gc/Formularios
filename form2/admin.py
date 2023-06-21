from django.contrib import admin
from .models import Projeto

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_criacao')


