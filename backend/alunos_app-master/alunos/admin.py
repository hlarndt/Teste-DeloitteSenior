from django.contrib import admin
from .models import *

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    pass

class DisciplinaAdmin(admin.ModelAdmin):
    pass

class BoletimAdmin(admin.ModelAdmin):
    pass

class NotasBoletimAdmin(admin.ModelAdmin):
    pass

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Boletim, BoletimAdmin)
admin.site.register(NotasBoletim, NotasBoletimAdmin)