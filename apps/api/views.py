from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from .models import Nota, Materia, Estudiante, MateriaEstudiante
from .serializers import NotaSerializer, MateriaSerializer, EstudianteSerializer, MatEstuSerializer
from rest_framework import serializers
from django.shortcuts import get_object_or_404


class MultipleFieldLookupMixin(object):

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field, None):
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class NotaViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    lookup_fields = ['estudiante_id', 'materia_id']
    serializer_class = NotaSerializer
    queryset = Nota.objects.all()


class MateriaViewSet(viewsets.ModelViewSet):
    lookup_field = 'nombre'
    serializer_class = MateriaSerializer
    queryset = Materia.objects.all()


class MateriaEstViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    lookup_fields = ['estudiante_id', 'materia_id']
    serializer_class = MatEstuSerializer
    queryset = MateriaEstudiante.objects.all()


class EstudianteViewSet(viewsets.ModelViewSet):
    lookup_field = 'cedula'
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()
