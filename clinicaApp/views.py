from django.shortcuts import render, redirect
from django.http import HttpResponse 
from clinicaApp.models import Paciente, Doctor, Especialidad, Agenda, FichaPaciente, Receta, Medicamentos, Tipousuario, Permiso
from .forms import AgendaForm
from django.contrib.auth.models import AbstractUser
from django.contrib import messages
from django.shortcuts import get_object_or_404
import re

# Create your views here.
#///////////////////// GENERALIDADES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def clinicaKill(request):
    return render(request,"inicio.html")

def inicio(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AgendaForm()
        doctores = Doctor.objects.all()
        especialidades = Especialidad.objects.all()
        equipo = Doctor.objects.all()  # Cambia Doctor por Doctor
        return render(request, 'inicio.html', {
        'form': form,
        'doctores': doctores,
        'especialidades': especialidades,
        'equipo': equipo,  # Ahora 'equipo' contiene los doctores
    })

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def equipo(request):
    equipo = Doctor.objects.all()
    return render(request, 'equipo.html', {'equipo': equipo})

def testimonios(request):
    testimonios = Testimonio.objects.all()
    return render(request, 'testimonios.html', {'testimonios': testimonios})

def contacto(request):
    if request.method == 'POST':
        # Procesa el formulario de contacto aquí
        pass
    return render(request, 'contacto.html')

def footer(request):
    return render(request, "footer.html")

def inicioSesion(request):
    return render(request, "login.html")

def about(request):
    return HttpResponse('About')    


#MODULOS FUNCIONES PARA VISTA INICIO

#*********************************************************************************************************
#*********************************************************************************************************
#///////////////////// VISTA INICIO, CRUD - VALIDACIONES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#********************************************************************************************************
#********************************************************************************************************

def agendar_cita(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AgendaForm()
    return render(request, 'agendar_cita.html', {'form': form})

#MODULOS FUNCIONES PARA PACIENTE

#*********************************************************************************************************
#*********************************************************************************************************
#///////////////////// PACIENTES, CRUD - VALIDACIONES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#********************************************************************************************************
#********************************************************************************************************

def crearPaciente(request):
    return render(request, "paci_nuevo.html")

def eliminarPaciente(request):
    pacientes = Paciente.objects.all() #pacientes es variable que guarda la consulta de la tabla paciente
    return render(request, "paci_borrar.html",{
    'pacientes' : pacientes
    })

def listarPaciente(request):
    pacientes = Paciente.objects.all() #pacientes es variable que guarda la consulta de la tabla paciente
    return render(request, "paci_listar.html",{ #creaciond e diccionarios para enviar los datos al template html que corresponde
        'pacientes' : pacientes
    })

def actualizarPaciente(request):
    pacientes = Paciente.objects.all()
    return render(request, "paci_actualizar.html",{
        'pacientes' : pacientes
    })

# def buscar_rut(rut):
#     existe_rut = Paciente.objects.filter(rut=rut).exists()
#     if existe_rut:
#         messages.error(request, 'Rut no disponible')
#     else:
#         messages.success(request, 'Rut disponible')
#         return redirect('listarPaciente')

#VALIDAR PUNTOS Y GUIÓN
def validar_rut(rut):
    rut_pattern = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]{1}$')
    rut_pattern_con_guion = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-\d{1}$')
    return bool(rut_pattern.match(rut)) or bool(rut_pattern_con_guion.match(rut))

#VALIDAR SOLO NUMEROS
def validar_rutstring(rut):
    if not re.match("^[0-9\-.]+$", rut):
        return False
    return True
#VAlidar nombre aceptar Ñ  y tilde solo letras
def validar_nombreapellido(string):
    if re.match('^[A-Za-záéíóúÁÉÍÚÓñÑ\s]+$', string):
        return True
    return False

#CREAR PACIENTE CON FUNCIONES DE VALIDACIONES 
def guardar(request):
    rut = request.POST["rut"]
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
    
    if validar_rutstring(rut):
        messages.success(request,'Rut Validado sin letras')        
    else:
        messages.error(request,"No se admiten letras en Rut")
        return redirect('listarPaciente')
    
    # Validar longitud máxima para el RUT
    if len(rut) < 2 or len(rut) > 12:
        messages.error(request, 'Rut Inválido.')
        return redirect('listarPaciente')   
 
    # Validar longitud máxima para nombre y dirección
    if len(nombre) > 100 or len(direccion) > 100:
        messages.error(request, 'Nombre y dirección no deben exceder los 100 caracteres.')
        return redirect('listarPaciente')
    
    if validar_nombreapellido(nombre):
        messages.success(request, 'Nombre Validado')
    else:
        messages.error(request, "Nombre incorrecto")
        return redirect('listarPaciente') 

    # Validar que el nombre y la dirección contengan solo letras y espacios
    if not (nombre.replace(" ", "").isalpha()):
        messages.error(request, 'Nombre solo deben contener letras y espacios.')
        return redirect('listarPaciente')   

    tipousuario_fk = get_object_or_404(Tipousuario, id_tipousuario=1)

    pa = Paciente(rut_paciente=rut, nombre_paciente=nombre, direccion_paciente=direccion,telefono_paciente=telefono,
                    correo_paciente=correo, tipousuario=tipousuario_fk)
    pa.save()
    messages.success(request, 'Paciente Guardado')
    return redirect('listarPaciente')

#/////////VALIDACIONES EN EDITAR PACIENTE\\\\\\\\\\\\\\\\\\\\\\\\

#Eliminar del listado con boton
def eliminar(request, rut_paciente):
    paciente = Paciente.objects.get(rut_paciente=rut_paciente)
    paciente.delete()
    messages.success(request, 'Paciente eliminado')
    return redirect('listarPaciente')

#listar para actualizar 
def detalle(request, rut_paciente):
    paciente = Paciente.objects.get(rut_paciente=rut_paciente)
    return render(request, "paciente_editar.html", {
        'paciente': paciente
    })



def editar(request):
    try:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        rut_paciente = request.POST["rut"]    
        # if validar_rutstring(rut):
        #     messages.success(request,'Rut Validado sin letras')        
        # else:
        #     messages.error(request,"No se admiten letras en Rut")
        #     return redirect('listarPaciente')
        
        # Validar longitud máxima para el RUT
        if len(rut) < 2 or len(rut) > 12:
            messages.error(request, 'Rut Inválido.')
            return redirect('listarPaciente')   
    
        # Validar longitud máxima para nombre y dirección
        if len(nombre) > 100 or len(direccion) > 100:
            messages.error(request, 'Nombre y dirección no deben exceder los 100 caracteres.')
            return redirect('listarPaciente')
        
        if validar_nombreapellido(nombre):
            messages.success(request, 'Nombre Validado')
        else:
            messages.error(request, "Nombre incorrecto")
            return redirect('listarPaciente') 

        # Validar que el nombre y la dirección contengan solo letras y espacios
        if not (nombre.replace(" ", "").isalpha()):
            messages.error(request, 'Nombre solo deben contener letras y espacios.')
            return redirect('listarPaciente')  
        
        paciente = get_object_or_404(Paciente, rut_paciente=rut_paciente)
        paciente.rut_paciente = rut
        paciente.rut_paciente = rut
        paciente.nombre_paciente = nombre
        paciente.direccion_paciente = direccion
        paciente.telefono_paciente = telefono
        paciente.correo_paciente = correo
        paciente.save()

        messages.success(request, 'Paciente Actualizado')
    except Exception as e:
            messages.error(request, f'Error: {e}')

    return redirect('listarPaciente')


#*********************************************************************************************************
#*********************************************************************************************************
#///////////////////// MÉDICOS, CRUD - VALIDACIONES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#********************************************************************************************************
#********************************************************************************************************

def crearDoctor(request):
    especialidades = Especialidad.objects.all()

    return render(request, "doctores_nuevos.html", {'lista_especialidades': especialidades})

def detalleDoctor(request, id_doctor):
    doctor = Doctor.objects.get(pk=id_doctor)
    return render(request, "doctores_editar.html", {
        'doctor': doctor
    })
    
# Listar doctores
def listarDoctor(request):
    doctores = Doctor.objects.all()  # Recuperar todos los médicos de la base de datos
    return render(request, 'doctores_listar.html', {'doctores': doctores})  # Pasar los médicos a la plantilla

def validar_idInt(id_doctor):
    # Esta función verifica si el id_doctor solo contiene números
    return id_doctor.isdigit()

def validar_nombreDoctor(nombre_doctor):
    # Esta expresión regular acepta letras, acentos, "ñ" y espacios, y es insensible a mayúsculas y minúsculas
    pattern = re.compile(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$')
    return bool(pattern.match(nombre_doctor))



def guardarDoctor(request):
    especialidades = Especialidad.objects.all()
    

    if request.method == 'POST':
        nombre_doctor = request.POST.get("nombre_doctor")
        titulo = request.POST.get("titulo")
        id_especialidad = request.POST.get("especialidad")
        correo = request.POST.get("correo_doctor")
        foto = request.FILES.get("foto", None)
        # id_agenda = request.POST.get("agenda")
        # agenda = get_object_or_404(Agenda, id_agenda=id_agenda)

        if len(nombre_doctor) > 100 or len(titulo) > 100:
            messages.error(request, 'Nombre, título del profesional, y especialidad no deben exceder los 100 caracteres.')
            return redirect('listarDoctor')

        if not validar_nombreDoctor(nombre_doctor):
            messages.error(request, "Nombre incorrecto")
            return redirect('listarDoctor') 

        # Verificar si la especialidad con el id proporcionado existe
        try:
            especialidad = Especialidad.objects.get(id_especialidad=id_especialidad)
        except Especialidad.DoesNotExist:
            messages.error(request, 'Especialidad no encontrada.')
            return redirect('listarDoctor')

        doc = Doctor(
            nombre_doctor=nombre_doctor,
            titulo=titulo,
            especialidad=especialidad,
            correo=correo,
            foto=foto
            # agenda=agenda
        )
        doc.save()
        messages.success(request, 'Doctor Guardado')
        return redirect('listarDoctor')

    else:
        # Obtener el valor de 'especialidad' directamente del QueryDict
        id_especialidad = request.POST.getlist("especialidad")
        form = especialidad(initial={'especialidad': id_especialidad}) 
        return render(request, "doctores_nuevos.html", {'form': form, 'lista_especialidades': especialidades})


# Eliminar doctor
def eliminarDoctor(request, id_doctor):
    doctor = Doctor.objects.get(pk=id_doctor)
    doctor.delete()
    messages.success(request, 'Doctor eliminado')
    return redirect('listarDoctor')

# Actualizar doctor
def actualizarDoctor(request, id_doctor):
    doctor = Doctor.objects.get(pk=id_doctor)
    if request.method == 'POST':
        doctor.nombre_doctor = request.POST["nombre_doctor"]
        doctor.titulo = request.POST["titulo"]
        doctor.id_especialidad = request.POST["especialidad"]
        doctor.correo = request.POST["correo_doctor"]
        doctor.foto = request.FILES["foto"] if 'foto' in request.FILES else doctor.foto

        doctor.save()
        messages.success(request, 'Doctor actualizado')
        return redirect('listarDoctor')
    else:
        return render(request, "doctores_actualizar.html",{
            'doctor' : doctor
        })

# Editar doctor
from django.shortcuts import get_object_or_404

def editarDoctor(request, id_doctor):
    try:
        doctor = Doctor.objects.get(pk=id_doctor)

        if request.method == 'POST':
            doctor.nombre_doctor = request.POST["nombre_doctor"]
            doctor.titulo = request.POST["titulo"]
            doctor.id_especialidad = request.POST["especialidad"]
            doctor.correo = request.POST["correo_doctor"]
            
            # Manejo de la foto, asegúrate de que request.FILES esté presente
            doctor.foto = request.FILES["foto"] if 'foto' in request.FILES else doctor.foto
            
            doctor.save()
            messages.success(request, 'Doctor actualizado')
            return redirect('listarDoctor')
        else:
            return render(request, "doctores_editar.html", {'doctor': doctor})
    except Doctor.DoesNotExist:
        messages.error(request, 'Doctor no encontrado')
        return redirect('listarDoctor')
    except Exception as e:
        messages.error(request, f'Error al actualizar doctor: {e}')
        return redirect('listarDoctor')


###ESPECIALIDAD
def listarespecialidad(request):
    especialidades = Especialidad.objects.all() 
    return render(request, "especialidades_listar.html",{
        'especialidades' : especialidades
    })