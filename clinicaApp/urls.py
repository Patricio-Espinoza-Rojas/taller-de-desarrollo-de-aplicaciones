from django.urls import path
from . import views 


urlpatterns = [
    path('', views.clinicaKill, name='clinica'),
    path('about/', views.about),  
    path('Crear Paciente', views.crearPaciente, name='crearPaciente'),
    path('Eliminar Paciente', views.eliminarPaciente, name='eliminarPaciente'),
    path('Listar Paciente', views.listarPaciente, name='listarPaciente'),
    path('Actualizar Paciente', views.actualizarPaciente, name='actualizarPaciente'),
    path('pacientes/guardar', views.guardar, name='guardar'),
    path('pacientes/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('pacientes/detalle/<int:id>', views.detalle, name='detalle'),
    path('pacientes/editar', views.editar, name='editar'),
    path('inicio sesion', views.inicioSesion, name='inicioSesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('footer/', views.footer, name='footer'),
]
