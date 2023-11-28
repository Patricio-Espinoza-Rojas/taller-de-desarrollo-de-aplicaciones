from django.shortcuts import render, redirect
from django.http import HttpResponse 
from clinicaApp.models import Paciente
from django.contrib import messages
import re

# Create your views here.
def clinicaKill(request):
    return render(request,"clinicaweb.html")

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

def validar_rut(rut):
    # Función para validar el formato del RUT chileno
    rut_pattern = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$')
    return bool(rut_pattern.match(rut))

#crear paciente
def guardar(request):
    rut = request.POST["rut"]
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]

    # Validar longitud máxima para nombre y dirección
    if len(nombre) > 100 or len(direccion) > 100:
        messages.error(request, 'Nombre y dirección no deben exceder los 100 caracteres.')
        return redirect('guardar')

    # Validar longitud máxima para el RUT
    if len(rut) > 10:
        messages.error(request, 'Rut No Válido.')
        return redirect('listarPaciente')

    # Validar que el nombre y la dirección contengan solo letras y espacios
    if not (nombre.replace(" ", "").isalpha() and direccion.replace(" ", "").isalpha()):
        messages.error(request, 'Nombre y dirección solo deben contener letras y espacios.')
        return redirect('guardar')

    # Validar el formato del RUT
    if not validar_rut(rut):
        messages.error(request, 'Rut No Válido.')
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
    direccion_paciente = request.POST["direccion"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
    id = request.POST["id"]
    
        # Validar que no se admitan caracteres especiales en el nombre y la dirección
    if not (nombre.replace(" ", "").isalnum() and direccion_paciente.replace(" ", "").isalnum()):
        messages.error(request, 'Nombre y dirección no deben contener caracteres especiales.')
        return redirect('listarPaciente')

    # Validar que el teléfono contenga solo números
    if not telefono.isdigit():
        messages.error(request, 'Teléfono solo debe contener números.')
        return redirect('listarPaciente')

    if len(rut) > 10:
        messages.error(request, 'Rut No Válido.')
        return redirect('listarPaciente')
    
    # if not validar_rut(rut):
    #     messages.error(request, 'Rut No Válido.')
    #     return redirect('listarPaciente')
    
    Paciente.objects.filter(pk=id).update(rut_paciente=rut, nombre_paciente=nombre, direccion_paciente=direccion_paciente,telefono_paciente=telefono,
                    correo_paciente=correo)
    messages.success(request, 'Paciente Actualizado')
    return redirect('listarPaciente')

    
    
    


