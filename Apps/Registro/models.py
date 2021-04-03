from django.db import models

# Create your models here.

class Alumno(models.Model):
    A_paterno = models.CharField(max_length=35)
    A_materno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Fecha_nacimiento = models.DateField()
    SEXOS = (('F','Femenino'),('M','Masculino'))
    sexo = models.CharField(max_length=1,choices=SEXOS,default='M')


    def NombreCompleto(self):
        cadena="{0} {1}, {2}"
        return cadena.format(self.A_paterno, self.A_materno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Curso(models.Model):
    Nombre = models.CharField(max_length=40)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} Disponible: ({1})".format(self.Nombre, self.Estado)

class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #pylint: disable=E1101
        cadena = "{0} -> {1}"
        return cadena.format(self.Alumno, self.Curso.Nombre)

        


