from django.db import models

# Create your models here.

class Patient(models.Model):
    """ id_paciente = models.CharField(max_length=10, unique=True) """
    nombre = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=(('m', 'Masculino'), ('f', 'Femenino')))
    fecha_ingreso = models.DateField()
    
    def __str__(self):
        return self.nombre

class MedicalTest(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    costo = models.FloatField()
    tiempo_resultado = models.DateField()

    def __str__(self):
        return self.nombre

class Result(models.Model):
    paciente = models.ForeignKey('Patient', on_delete=models.CASCADE)
    prueba = models.ForeignKey('MedicalTest', on_delete=models.CASCADE)
    fecha_resultado = models.DateField()
    resultado = models.CharField(max_length=255)

    def __str__(self):
        return f'Resultado para {self.paciente.nombre} - {self.prueba.nombre}'