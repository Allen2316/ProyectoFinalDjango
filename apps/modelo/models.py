from django.db import models


class Materia(models.Model):
    materia_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, null=True, blank=True)    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)


class Estudiante(models.Model):
    listaGenero = (
        ('femenino', 'Femenino'),
        ('masculino', 'Masculino')
    )

    listaEstadoCivil = (
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo'),
        ('separado', 'Separado'),
    )
    estudiante_id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, unique=True, null=False)
    nombres = models.CharField(max_length=70, null=False)
    apellidos = models.CharField(max_length=70)
    genero = models.CharField(
        max_length=20, choices=listaGenero, default="femenino")
    estadoCivil = models.CharField(
        max_length=20, choices=listaEstadoCivil, default="soltero")
    correo = models.CharField(max_length=105)
    celular = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    # blank=True permite dejar vacio o en blanco
    materia = models.ManyToManyField(Materia, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cedula


class Nota(models.Model):
    nota_id = models.AutoField(primary_key=True)
    nota1 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    nota2 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    nota3 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    promedio = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nota_id)


class MateriaEstudiante(models.Model):
    matEst_id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.matEst_id)
