from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Patient, MedicalTest, Result
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse

# Create your views here.

class PatientView(View):

    # método get
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id > 0):
            patients = list(Patient.objects.filter(id=id).values())
            if len(patients) > 0:
                patient = patients[0]
                datos = {'estatus': 'true', 
                        'datos': patient}
            else:
                datos = {'message': "patients not found..."}
            return JsonResponse(datos)
        else:
            patients = list(Patient.objects.values())
            if len(patients) > 0:
                #{'message': "Success", 'patients': patients}
                datos = {'estatus': 'true', 
                        'datos': { 'current_page': 1,
                                    'data' : patients}
                        }
            else:
                datos = {'message': "patients not found..."}
            return JsonResponse(datos)

    # método post
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Patient.objects.create(nombre=jd['nombre'],
                            edad=jd['edad'],
                            fecha_ingreso=jd['fecha_ingreso'],
                            genero=jd['genero'])
        datos = {'estatus': 'true',
                'message': "Registro creado"}
        return JsonResponse(datos)

    # método put
    def put(self, request, id):
        jd = json.loads(request.body)
        patients = list(Patient.objects.filter(id=id).values())
        if len(patients) > 0:
            # Modelo.objects.get no busca obtiene algo seguro.
            patient = Patient.objects.get(id=id)
            patient.nombre = jd['nombre']
            patient.edad = jd['edad']
            patient.genero = jd['genero']
            patient.fecha_ingreso = jd['fecha_ingreso']
            patient.save()
            datos = {'estatus': 'true',
                    'message': "Actualizado"}
        else:
            datos = {'message': "patient not found..."}
        return JsonResponse(datos)

    # método delete
    def delete(self, request, id):
        patients = list(Patient.objects.filter(id=id).values())
        if len(patients) > 0:
            Patient.objects.filter(id=id).delete()
            datos = {'estatus': 'true',
                    'message': "Eliminado"}
        else:
            datos = {'message': "patient not found..."}
        return JsonResponse(datos)
    

class MedicalTestView(View):

    # método get
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id > 0):
            pruebas = list(MedicalTest.objects.filter(id=id).values())
            if len(pruebas) > 0:
                patient = pruebas[0]
                datos = {'estatus': 'true', 
                        'datos': patient}
            else:
                datos = {'message': "patients not found..."}
            return JsonResponse(datos)
        else:
            pruebas = list(MedicalTest.objects.values())
            if len(pruebas) > 0:
                #{'message': "Success", 'patients': patients}
                datos = {'estatus': 'true', 
                        'datos': { 'current_page': 1,
                                    'data' : pruebas}
                        }
            else:
                datos = {'message': "patients not found..."}
            return JsonResponse(datos)

    # método post
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        MedicalTest.objects.create(
                            nombre=jd['nombre'],
                            tipo=jd['tipo'],
                            costo=jd['costo'],
                            tiempo_resultado=jd['tiempo_resultado'])
        datos = {'estatus': 'true',
                'message': "Registro creado"}
        return JsonResponse(datos)

    # método put
    def put(self, request, id):
        jd = json.loads(request.body)
        pruebas = list(MedicalTest.objects.filter(id=id).values())
        if len(pruebas) > 0:
            # Modelo.objects.get no busca obtiene algo seguro.
            prueba = MedicalTest.objects.get(id=id)
            prueba.nombre = jd['nombre']
            prueba.tipo = jd['tipo']
            prueba.costo = jd['costo']
            prueba.tiempo_resultado = jd['tiempo_resultado']
            prueba.save()
            datos = {'estatus': 'true',
                    'message': "Actualizado"}
        else:
            datos = {'message': "patient not found..."}
        return JsonResponse(datos)

    # método delete
    def delete(self, request, id):
        pruebas = list(MedicalTest.objects.filter(id=id).values())
        if len(pruebas) > 0:
            MedicalTest.objects.filter(id=id).delete()
            datos = {'estatus': 'true',
                    'message': "Eliminado"}
        else:
            datos = {'message': "patient not found..."}
        return JsonResponse(datos)
    

class ResultView(View):

    # método get
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id > 0):
            resultados = list(Result.objects.filter(id=id).values())

            if len(resultados) > 0:
                patient = resultados[0]
                datos = {'estatus': 'true', 
                        'datos': patient}
            else:
                datos = {'message': "patients not found..."}
            return JsonResponse(datos)
        else:
            resultados = list(Result.objects.values())

            if len(resultados) > 0:
                #{'message': "Success", 'patients': patients}
                datos = {'estatus': 'true', 
                        'datos': { 'current_page': 1,
                                    'data' : resultados}
                        }
            else:
                datos = {'message': "resultados not found..."}

            return JsonResponse(datos)

    # método post
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        try:
            paciente = Patient.objects.get(id=jd['id_paciente'])
            prueba = MedicalTest.objects.get(id=jd['id_prueba'])
        except Patient.DoesNotExist:
            return JsonResponse({'status':'false','message':'no existe paciente o prueba medica'})

        Result.objects.create(
                            paciente=paciente,
                            prueba=prueba,
                            fecha_resultado=jd['fecha_resultado'],
                            resultado=jd['resultado'])
        datos = {'estatus': 'true',
                'message': "Registro creado"}
        return JsonResponse(datos)

    # método put
    def put(self, request, id):
        jd = json.loads(request.body)
        resultados = list(Result.objects.filter(id=id).values())
        if len(resultados) > 0:
            # Modelo.objects.get no busca obtiene algo seguro.
            resultado = Result.objects.get(id=id)
            resultado.paciente = jd['id_paciente']
            resultado.prueba = jd['id_prueba']
            resultado.fecha_resultado = jd['fecha_resultado']
            resultado.resultado = jd['resultado']
            resultado.save()
            datos = {'estatus': 'true',
                    'message': "Actualizado"}
        else:
            datos = {'message': "patient not found..."}
        return JsonResponse(datos)

    # método delete
    def delete(self, request, id):
        pruebas = list(Result.objects.filter(id=id).values())
        if len(pruebas) > 0:
            Result.objects.filter(id=id).delete()
            datos = {'estatus': 'true',
                    'message': "Eliminado"}
        else:
            datos = {'message': "patient not found..."}
        return JsonResponse(datos)
    