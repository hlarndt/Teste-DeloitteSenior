import datetime
from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    data_aniversario = models.DateField(auto_now=False,
                                     auto_now_add=False)
    def __unicode__(self):
        return u'%s %s' % (self.nome, self.email, self.data_aniversario)

    def __str__(self):
        return f"{self.nome}, {self.email}, "+datetime.datetime.strftime(self.data_aniversario,"%d/%m/%Y")

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.nome, self.carga_horaria)

    def __str__(self):
        return f"{self.nome}, {self.carga_horario}"

class Boletim(models.Model):
    data_entrega = models.DateField(auto_now=False,
                                     auto_now_add=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.data_entrega, self.aluno)

    def __str__(self):
        return f""+datetime.datetime.strftime(self.data_entrega,"%d/%m/%Y")+", {self.aluno}"

class NotasBoletim(models.Model):
    boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True)
    nota = models.FloatField()

    def __unicode__(self):
        return u'%s %s' % (self.boletim, self.disciplina, self.nota)
    
    def __str__(self):
        return f"{self.boletim}, {self.disciplina}, {self.nota}"
