from django.shortcuts import render, redirect
from django.http import HttpResponse 
from clinicaApp.models import Paciente
from django.contrib import messages
import re

# Create your views here.
def clinicaKill(request):
    return render(request,"inicio.html")

def inicio(request):
    return render(request, "inicio.html")

def footer(request):
    return render(request, "footer.html")

def inicioSesion(request):
    return render(request, "login.html")

def about(request):
    return HttpResponse('About')    

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

    
    
    


