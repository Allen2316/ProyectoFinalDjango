from django.urls import path
from . import views

urlpatterns = [
    # estudiantes
    path('', views.index, name="estudiantes"),
    path('crearEstudiante/', views.crearEstudiante, name="crearEstudiante"),
    path('updateEstudiante/<str:cedula>/', views.actualizarEstudiante, name="updateEstudiante"),
    path('deleteEstudiante/<str:cedula>/', views.eliminarEstudiante, name="deleteEstudiante"),
    #? MATERIAS
    path('crearMateria/', views.crearMateria, name="crearMateria"),
    path('materias/<str:cedula>/', views.listarMaterias, name="materias"),
    path('updateMateria/<str:nombre>/', views.actualizarMateria, name="updateMateria"),
    path('deleteMateria/<str:nombre>/', views.eliminarMateria, name="deleteMateria"),
    
    #? NOTAS
    path('Notas/<str:cedula>/<str:nombre>/', views.asigNotas, name="Notas"),
    
]
