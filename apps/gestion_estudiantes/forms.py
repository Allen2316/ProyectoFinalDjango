from django import forms
from django.views.generic.edit import UpdateView
from apps.modelo.models import Estudiante, Materia, Nota, MateriaEstudiante


class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['cedula', 'apellidos', 'nombres',
                  'genero', 'estadoCivil', 'correo', 'celular', 'direccion', 'materia']

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'estadoCivil': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'materia': forms.CheckboxSelectMultiple(),
        }


class FrmEstudianteUpdate(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['cedula', 'apellidos', 'nombres',
                  'genero', 'estadoCivil', 'correo', 'celular', 'direccion', 'materia']

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'estadoCivil': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'materia': forms.CheckboxSelectMultiple(),
        }


class FormularioMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class FormularioNotas(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nota1', 'nota2', 'nota3', 'promedio', ]
        widgets = {
            'nota1': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nota2': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nota3': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'promedio': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }


class FormularioMatEst(forms.ModelForm):
    class Meta:
        model = MateriaEstudiante
        fields = ['estado', ]
        widgets = {
            'estado': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }
