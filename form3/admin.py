from django.contrib import admin
from .models import Curso,Projeto

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display=('nome','descricao','curso')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display=('nome',)