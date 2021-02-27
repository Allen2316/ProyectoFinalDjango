from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.modelo.models import Nota, Materia, Estudiante, MateriaEstudiante


class NotaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Nota
        fields = '__all__'


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'



class MatEstuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaEstudiante
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
        