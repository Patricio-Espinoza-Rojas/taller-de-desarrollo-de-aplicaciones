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
    path('servicios/', views.servicios, name='servicios'),
    path('equipo/', views.equipo, name='equipo'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('contacto/', views.contacto, name='contacto'),
    path('footer/', views.footer, name='footer'),
    path('Ingresar Doctor', views.ingresarDoctor, name='ingresarDoctor'),
    path('Eliminar Doctor', views.eliminarDoctor, name='eliminarDoctor'),
    path('Listar Doctor', views.listarDoctor, name='listarDoctor'),
    path('Actualizar Doctor', views.actualizarDoctor, name='actualizarDoctor'),
    path('Doctor/guardar_doctor', views.guardar_doctor, name='guardar_doctor'),
    path('Doctor/eliminar_doctor/<int:id_doctor>', views.eliminar_doctor, name='eliminar_doctor'),
    path('Doctor/detalle_doctor/<int:id_doctor>', views.detalle_doctor, name='detalle_doctor'),
    path('Doctor/editar_doctor', views.editar_doctor, name='editar_doctor'),
]
