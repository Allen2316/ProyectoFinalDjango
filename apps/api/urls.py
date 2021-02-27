from django.contrib import admin
from django.urls import path, include
from . import views



listaNParametros = views.NotaViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

listaM = views.MateriaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

listaMParametros = views.MateriaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

listaE = views.EstudianteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

listaEParametros = views.EstudianteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


listaMEParametros = views.MateriaEstViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('getNota/<int:estudiante_id>/<int:materia_id>/', listaNParametros, name='lista-notas-parametros'),
    
    path('getMateria/', listaM, name='lista-materias'),
    path('getMateria/<str:nombre>/', listaMParametros, name='lista-materias-parametros'),
    
    path('getEstudiante/', listaE, name='lista-estudiantes'),
    path('getEstudiante/<str:cedula>/', listaEParametros, name='lista-estudiantes-parametros'),
    
    path('getME/<int:estudiante_id>/<int:materia_id>/', listaMEParametros, name='lista-ME-parametros'),

    
]
