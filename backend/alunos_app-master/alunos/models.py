from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    data_aniversario = models.DateField(auto_now=False,
                                     auto_now_add=False)

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()

class Boletim(models.Model):
    data_entrega = models.DateField(auto_now=False,
                                     auto_now_add=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    
class NotasBoletim(models.Model):
    boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.FloatField()
