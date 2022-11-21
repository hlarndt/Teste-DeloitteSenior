from django.urls import path
from alunos import views

urlpatterns = [
    path('aluno/', views.AlunoList.as_view()),
    path('disciplina/', views.DisciplinaList.as_view()),
    path('boletim/', views.BoletimList.as_view()),
    path('boletim_notas/', views.NotasBoletimList.as_view()),
]
