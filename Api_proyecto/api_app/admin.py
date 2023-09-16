from django.contrib import admin
from .models import Patient, MedicalTest, Result

# Register your models here.
# Registrar el modelo Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'genero', 'fecha_ingreso')

# Registrar el modelo MedicalTest
@admin.register(MedicalTest)
class MedicalTestAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'costo', 'tiempo_resultado')

# Registrar el modelo Result
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'prueba', 'fecha_resultado', 'resultado')