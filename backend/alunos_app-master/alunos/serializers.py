from rest_framework import serializers

from .models import *


class AlunoSerializer(serializers.ModelSerializer):
    """Serializer of Aluno model for API processing"""
    class Meta:
        model = Aluno
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    """Serializer of Disciplina model for API processing"""
    class Meta:
        model = Disciplina
        fields = '__all__'

class BoletimSerializer(serializers.ModelSerializer):
    """Serializer of Boletim model for API processing"""
    class Meta:
        model = Boletim
        fields = '__all__'

class NotasBoletimSerializer(serializers.ModelSerializer):
    """Serializer of Notas Boletim model for API processing"""
    class Meta:
        model = NotasBoletim
        fields = '__all__'
