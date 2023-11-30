from django.shortcuts import render, redirect
from django.http import HttpResponse 
from clinicaApp.models import Paciente, Doctor
from django.contrib import messages
import re

# Create your views here.
#///////////////////// GENERALIDADES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def clinicaKill(request):
    return render(request,"inicio.html")

def inicio(request):
    return render(request, "inicio.html")

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def equipo(request):
    equipo = Medico.objects.all()
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


#///////////////////// PACIENTES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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

#///////////////////// MÉDICOS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def ingresarDoctor(request):
    doctor = Doctor.objects.all()
    return render(request, "medicos_nuevos.html",{
        'doctor' : doctor
    })

def eliminarDoctor(request):
    doctor = Doctor.objects.all()
    return render(request, "medicos_borrar.html",{
        'doctor' : doctor
    })

def listarDoctor(request):
    doctor = Doctor.objects.all()
    return render(request, "medicos_listar.html",{
        'doctor' : doctor
    })

def actualizarDoctor(request):
    doctor = Doctor.objects.all()
    return render(request, "medicos_actualizar.html",{
        'doctor' : doctor
    })



#/////////////////////// VALIDACIONES\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def buscar_rut(rut):
#     existe_rut = Paciente.objects.filter(rut=rut).exists()
#     if existe_rut:
#         messages.error(request, 'Rut no disponible')
#     else:
#         messages.success(request, 'Rut disponible')
#         return redirect('listarPaciente')

def validar_rut(rut):
    rut_pattern = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]{1}$')
    rut_pattern_con_guion = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-\d{1}$')
    return bool(rut_pattern.match(rut)) or bool(rut_pattern_con_guion.match(rut))

def validar_rutstring(rut):
    if not re.match("^[0-9\-]+$", rut):
        return False
    return True

def validar_nombre(string):
    if re.match('^[A-Za-záéíóúÁÉÍÚÓñÑ\s]+$', string):
        return True
    return False

#crear paciente CON VALIDACIONES ????????????????
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
    
    if validar_nombre(nombre):
        messages.success(request, 'Nombre Validado')
    else:
        messages.error(request, "Nombre incorrecto")
        return redirect('listarPaciente') 

    # Validar que el nombre y la dirección contengan solo letras y espacios
    if not (nombre.replace(" ", "").isalpha()):
        messages.error(request, 'Nombre solo deben contener letras y espacios.')
        return redirect('listarPaciente')   
    
    pa = Paciente(rut_paciente=rut, nombre_paciente=nombre, direccion_paciente=direccion,telefono_paciente=telefono,
                    correo_paciente=correo)
    pa.save()
    messages.success(request, 'Paciente Guardado')
    return redirect('listarPaciente')

def eliminar(request, id):
    paciente = Paciente.objects.filter(pk=id)
    paciente.delete()
    messages.success(request, 'Paciente eliminado')
    return redirect('listarPaciente')

def detalle(request, id):
    paciente = Paciente.objects.get(pk=id)
    return render(request, "paciente_editar.html",{
        'paciente' : paciente
    })

def editar(request):
    rut = request.POST["rut"]
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
    id = request.POST["id"]
    
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
    
    if validar_nombre(nombre):
        messages.success(request, 'Nombre Validado')
    else:
        messages.error(request, "Nombre incorrecto")
        return redirect('listarPaciente') 

    # Validar que el nombre y la dirección contengan solo letras y espacios
    if not (nombre.replace(" ", "").isalpha()):
        messages.error(request, 'Nombre solo deben contener letras y espacios.')
        return redirect('listarPaciente')   
    
    Paciente.objects.filter(pk=id).update(rut_paciente=rut, nombre_paciente=nombre, direccion_paciente=direccion,telefono_paciente=telefono,
                    correo_paciente=correo)
    messages.success(request, 'Paciente Actualizado')
    return redirect('listarPaciente')





#\\\\\\\\\\\\\\\\\ VALIDACIONES DOCTOR\\\\\\\\\\\\\\\\\\\\\    


def validar_idDoctor(id_doctor):
    id_pattern = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]{1}$')
    id_pattern_solo_numeros = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-\d{1}$')
    return bool(id_pattern.match(id_doctor)) or bool(id_pattern_solo_numeros.match(id_doctor))

def validar_idString(id_doctor):
    if not re.match("^[0-9\-]+$", id_doctor):
        return False
    return True

def validar_nombreDoctor(string):
    if re.match('^[A-Za-záéíóúÁÉÍÚÓñÑ\s]+$', string):
        return True
    return False



#\\\\\\\\\\\\\\\\\\\\\CREAR DOCTOR CON VALIDACIONES\\\\\\\\\\\\\\\\\\\\\\\\\    
    
def guardar_doctor(request):
    id_doctor = request.POST["id_doctor"]
    nombre_doctor = request.POST["nombre_doctor"]
    titulo = request.POST["titulo"]
    id_especialidad = request.POST["especialidad"]
    correo = request.POST["correo_doctor"]
    
    if validar_idString(id_doctor):
        messages.success(request,'Id Validado sin letras')        
    else:
        messages.error(request,"No se admiten letras en id")
        return redirect('listarDoctor')
    
    # Validar longitud máxima para el ID
    if len(id_doctor) < 2 or len(id_doctor) > 12:
        messages.error(request, 'Id Inválido.')
        return redirect('listarDoctor')   
 
    # Validar longitud máxima para nombre, Título profesional y especialidad
    if len(nombre_doctor) > 100 or len(titulo) :
        messages.error(request, 'Nombre, título del profesional, y especialidad no deben exceder los 100 caracteres.')
        return redirect('listarDoctor')
    
    if validar_nombre(nombre_doctor):
        messages.success(request, 'Nombre Validado')
    else:
        messages.error(request, "Nombre incorrecto")
        return redirect('listarDoctor') 

    # Validar que el nombre nombre, Título profesional y especialidad contengan solo letras y espacios
    if not (nombre_doctor.replace(" ", "").isalpha()):
        messages.error(request, 'Nombre solo deben contener letras y espacios.')
        return redirect('listarDoctor')   
    
    doc = Doctor(id_doctor=id_doctor, nombre_doctor=nombre_doctor, titulo=titulo,id_especialidad=id_especialidad, 
                correo=correo)
    doc.save()
    messages.success(request, 'Doctor Guardado')
    return redirect('listarDoctor')

def eliminar_doctor(request, id_doctor):
    doctor = Doctor.objects.filter(pk=id_doctor)
    doctor.delete()
    messages.success(request, 'Doctor eliminado')
    return redirect('listarDoctor')

def detalle_doctor(request, id_doctor):
    doctor = Doctor.objects.get(pk=id_doctor)
    return render(request, "medicos_editar.html",{
        'medico' : medico
    })

def editar_doctor(request):
    id_doctor = request.POST["id_doctor"]
    nombre_doctor = request.POST["nombre_doctor"]
    titulo_profesional = request.POST["titulo"]
    id_especialidad = request.POS["especialidad"]
    correo_doctor = request.POST["correo_doctor"]

