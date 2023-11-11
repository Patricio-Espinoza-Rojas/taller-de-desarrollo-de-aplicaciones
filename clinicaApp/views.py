from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def clinicaKill(request):
    return HttpResponse("<h1>Clínica Kill Coronavirus</h1>")

def about(request):
    return HttpResponse('About')    
