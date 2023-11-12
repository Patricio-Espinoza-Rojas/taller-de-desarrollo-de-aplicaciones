from django.urls import path
from . import views 


urlpatterns = [
    path('', views.clinicaKill, name='clinica'),
    path('about/', views.about),  
    path('Crear Paciente', views.crearPaciente, name='crearPaciente'),
    path('Eliminar Paciente', views.eliminarPaciente, name='borrarPaciente'),
    path('Listar Paciente', views.listarPaciente, name='listarPaciente'),
    path('Actualizar Paciente', views.actualizarPaciente, name='actualizarPaciente'),
    path('pacientes/guardar', views.guardar, name='guardar'),
]
