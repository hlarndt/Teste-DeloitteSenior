from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class AlunoList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    #permission_classes = (IsAuthenticated,)

class DisciplinaList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #permission_classes = (IsAuthenticated,)

class BoletimList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Boletim.objects.all()
    serializer_class = BoletimSerializer
    #permission_classes = (IsAuthenticated,)

class NotasBoletimList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = NotasBoletim.objects.all()
    serializer_class = NotasBoletimSerializer
    #permission_classes = (IsAuthenticated,)
