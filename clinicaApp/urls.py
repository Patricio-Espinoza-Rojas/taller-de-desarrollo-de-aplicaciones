from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/inicio/')),   
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
    path('agendar cita/', views.agendarCita, name='agendarCita'),
    path('Agendar Cita/', views.agendarCita, name='agendarCita'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('equipo/', views.equipo, name='equipo'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('contacto/', views.contacto, name='contacto'),
    path('footer/', views.footer, name='footer'),
    path('Crear Doctores', views.crearDoctor, name='crearDoctor'),
    path('Eliminar/Doctor/<int:id_doctor>', views.eliminarDoctor, name='eliminarDoctor'),
    path('Listar/Doctor', views.listarDoctor, name='listarDoctor'),
    path('Actualizar Doctor', views.actualizarDoctor, name='actualizarDoctor'),
    path('Especialidad/listarespecialidad', views.listarespecialidad, name='listarespecialidad'),
    path('doctor/detalle/<int:id_doctor>', views.detalleDoctor, name='detalle_doctor'),
    path('doctores/editar/<int:id_doctor>', views.editarDoctor, name='editarDoctor'),
    path('doctor/guardar', views.guardarDoctor, name='guardar_doctor'),
    path('receta/crear', views.crearReceta, name='crearReceta'),
    path('exportar_a_pdf/<int:receta_id>/', views.exportar_pdf, name='exportar_pdf'),
    path('Crear ficha paciente', views.crearFichaPaciente, name='crearFichaPaciente'),
    path('Listar ficha paciente', views.listarFichaPaciente, name='listarFichaPaciente'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)