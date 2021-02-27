from django.contrib import admin
from apps.modelo.models import Nota, Materia, Estudiante, MateriaEstudiante

admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Nota)
admin.site.register(MateriaEstudiante)
