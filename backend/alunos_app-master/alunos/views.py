from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import generics
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import AccessToken
from .models import *
from .serializers import *

@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
class AlunoList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView): 
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
class DisciplinaList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
class BoletimList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Boletim.objects.all()
    serializer_class = BoletimSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
class NotasBoletimList(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = NotasBoletim.objects.all()
    serializer_class = NotasBoletimSerializer
