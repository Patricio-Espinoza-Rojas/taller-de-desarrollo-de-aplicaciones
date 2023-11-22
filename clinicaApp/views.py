from django.shortcuts import render, redirect
from django.http import HttpResponse 
from clinicaApp.models import Paciente
from django.contrib import messages

# Create your views here.
def clinicaKill(request):
    return render(request,"clinicaweb.html")

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

def guardar(request):
    rut = request.POST["rut"]
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
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
    Paciente.objects.filter(pk=id).update(rut_paciente=rut, nombre_paciente=nombre, direccion_paciente=direccion_paciente,telefono_paciente=telefono,
                  correo_paciente=correo)
    messages.success(request, 'Paciente Actualizado')
    return redirect('listarPaciente')

    
    
    


