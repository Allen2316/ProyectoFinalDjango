from django.contrib import admin
from .models import Nota, Estudiante, Materia, MateriaEstudiante

admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Nota)
admin.site.register(MateriaEstudiante)
