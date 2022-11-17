from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from alunos import views

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view()),    
    path('refresh-token/', jwt_views.TokenRefreshView.as_view()),
    path('aluno/', views.AlunoList.as_view()),
    path('disciplina/', views.DisciplinaList.as_view()),
    path('boletim/', views.BoletimList.as_view()),
    path('boletim_notas/', views.NotasBoletimList.as_view()),
]
