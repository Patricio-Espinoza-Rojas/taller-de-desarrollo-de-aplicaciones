from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def clinicaKill(request):
    return render(request,"clinicaweb.html")

def about(request):
    return HttpResponse('About')    

def crearPaciente(request):
    return render(request, "paci_nuevo.html")

def eliminarPaciente(request):
    return render(request, "paci_borrar.html")

def listarPaciente(request):
    return render(request, "paci_listar.html")

def actualizarPaciente(request):
    return render(request, "paci_actualizar.html")

