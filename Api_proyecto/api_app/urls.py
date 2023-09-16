from django.urls import path
from .views import PatientView, MedicalTestView, ResultView

urlpatterns = [
    path('pacientes/', PatientView.as_view(), name='patients_list'),
    path('pacientes/<int:id>', PatientView.as_view(), name='patients_process'),

    path('p-medicas/', MedicalTestView.as_view(), name='medical-tests_list'),
    path('p-medicas/<int:id>', MedicalTestView.as_view(), name='medical-tests_process'),

    path('resultados/', ResultView.as_view(), name='results_list'),
    path('resultados/<int:id>', ResultView.as_view(), name='results_process'),
]
