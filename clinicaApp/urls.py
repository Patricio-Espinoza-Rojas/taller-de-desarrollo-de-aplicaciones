from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.clinicaKill, name='clinica'),
    path('about/', views.about),  
    path('Crear Paciente', views.crearPaciente, name='crearPaciente'),
    path('Eliminar Paciente', views.eliminarPaciente, name='eliminarPaciente'),
    path('Listar Paciente', views.listarPaciente, name='listarPaciente'),
    path('Actualizar Paciente', views.actualizarPaciente, name='actualizarPaciente'),
    path('pacientes/guardar', views.guardar, name='guardar'),
    path('pacientes/eliminar/<str:rut_paciente>', views.eliminar, name='eliminar'),
    path('pacientes/detalle/<str:rut_paciente>', views.detalle, name='detalle'),
    path('pacientes/editar', views.editar, name='editar'),
    path('inicio sesion', views.inicioSesion, name='inicioSesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('equipo/', views.equipo, name='equipo'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('contacto/', views.contacto, name='contacto'),
    path('footer/', views.footer, name='footer'),
    path('Crear Doctores', views.crearDoctor, name='crearDoctor'),
    path('Eliminar/Doctor/<int:id>', views.eliminarDoctor, name='eliminarDoctor'),
    path('Listar/Doctor', views.listarDoctor, name='listarDoctor'),
    path('Actualizar Doctor', views.actualizarDoctor, name='actualizarDoctor'),
    path('Especialidad/listarespecialidad', views.listarespecialidad, name='listarespecialidad'),
    path('doctor/detalle/<int:id>', views.detalleDoctor, name='detalle_doctor'),
    path('doctor/guardar', views.guardarDoctor, name='guardar_doctor'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)