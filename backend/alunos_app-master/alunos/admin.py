from django.contrib import admin
from .models import *

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_aniversario')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')

class BoletimAdmin(admin.ModelAdmin):
    list_display = ('data_entrega', 'aluno')

class NotasBoletimAdmin(admin.ModelAdmin):
    list_display = ('boletim', 'disciplina', 'nota')

admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Boletim,BoletimAdmin)
admin.site.register(NotasBoletim, NotasBoletimAdmin)
