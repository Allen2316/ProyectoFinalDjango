from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from apps.modelo.models import Estudiante, Materia, Nota, MateriaEstudiante
from .forms import FormularioEstudiante, FormularioMateria, FormularioNotas, FormularioMatEst, FrmEstudianteUpdate
from django.db.models import Q


def index(request):
    listaEstudiantes = Estudiante.objects.all()
    materias = Materia.objects.all()
    return render(request, 'estudiantes/index.html', locals())


def crearEstudiante(request):
    formulario_Estudiante = FormularioEstudiante(request.POST)
    if request.method == 'POST':
        if formulario_Estudiante.is_valid():
            formulario_Estudiante.save()
        return redirect(index)
    else:
        formulario_Estudiante = FormularioEstudiante()
    return render(request, 'estudiantes/crearEstudiantes.html', locals())


def actualizarEstudiante(request, cedula):
    estudiante = Estudiante.objects.get(cedula=cedula)
    if request.method == 'GET':
        formulario_Estudiante = FrmEstudianteUpdate(instance=estudiante)
    else:
        formulario_Estudiante = FrmEstudianteUpdate(
            request.POST, instance=estudiante)
        if formulario_Estudiante.is_valid():
            formulario_Estudiante.save()
        return redirect('materias', cedula)
    return render(request, 'estudiantes/modificar.html', locals())


def eliminarEstudiante(request, cedula):
    estudiante = Estudiante.objects.get(cedula=cedula)
    if request.method == 'POST':
        estudiante.delete()
        return redirect(index)
    return render(request, 'estudiantes/eliminar.html', locals())


# ? Vistas de Materias A PARTIR DE AQUI


def crearMateria(request):
    formulario_materia = FormularioMateria(request.POST)
    if request.method == 'POST':
        if formulario_materia.is_valid():
            formulario_materia.save()
        return redirect(index)
    else:
        formularioMateria = FormularioMateria()
    return render(request, 'materias/crearMaterias.html', locals())


def listarMaterias(request, cedula):
    estudiante = Estudiante.objects.filter(cedula=cedula).first()
    materias = estudiante.materia.all()
    notas = Nota.objects.filter(estudiante=estudiante)
    mateEst = MateriaEstudiante.objects.filter(estudiante=estudiante)
    return render(request, 'materias/index.html', locals())


def actualizarMateria(request, nombre):
    materia = Materia.objects.get(nombre=nombre)
    if request.method == 'GET':
        formulario_materia = FormularioMateria(instance=materia)
    else:
        formulario_materia = FormularioMateria(request.POST, instance=materia)
        if formulario_materia.is_valid():
            formulario_materia.save()
        return redirect(index)
    return render(request, 'materias/modificar.html', locals())


def eliminarMateria(request, nombre):
    materia = Materia.objects.get(nombre=nombre)
    if request.method == 'POST':
        materia.delete()
        return redirect(index)
    return render(request, 'materias/eliminar.html', locals())


def asigNotas(request, cedula, nombre):
    estudiante = Estudiante.objects.get(cedula=cedula)
    materia = Materia.objects.get(nombre=nombre)
    mateEst = MateriaEstudiante.objects.filter(
        materia=materia).filter(estudiante=estudiante).first()
    notas = Nota.objects.filter(materia=materia).filter(
        estudiante=estudiante).first()

    if request.method == 'GET' and notas:
        formulario_notasMate = FormularioNotas(instance=notas)
        formulario_EM = FormularioMatEst(instance=mateEst)
    else:
        if not Nota.objects.filter(materia=materia).filter(estudiante=estudiante).exists():
            notas = Nota()
            mateEst = MateriaEstudiante()

        formulario_notasMate = FormularioNotas(request.POST)
        if request.method == 'POST':
            if formulario_notasMate.is_valid():
                datos_nota = formulario_notasMate.cleaned_data
                not1 = datos_nota.get("nota1")
                not2 = datos_nota.get("nota2")
                not3 = datos_nota.get("nota3")
                notas.nota1 = float(not1)
                notas.nota2 = float(not2)
                notas.nota3 = float(not3)
                prome = float((not1+not2+not3)/3)
                notas.promedio = (prome)
                if prome >= 7:
                    mateEst.estado = "Aprobada"
                else:
                    mateEst.estado = "Reprobada"
                notas.estudiante = estudiante
                notas.materia = materia
                mateEst.materia = materia
                mateEst.estudiante = estudiante
                notas.save()
                mateEst.save()
            return redirect('materias', cedula)
        else:
            formulario_notasMate = FormularioNotas()
    return render(request, 'materias/AsigNota.html', locals())



