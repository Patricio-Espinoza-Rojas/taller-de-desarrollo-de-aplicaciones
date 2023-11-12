from django.db import models

# Create your models here.
#para tambien tener los aprametros con sql
class Paciente(models.Model):#tabla llamada paciente
    
    rut_paciente = models.CharField(max_length=9)
    nombre_paciente = models.CharField(max_length=150)
    direccion_paciente = models.CharField(max_length=200)
    telefono_paciente = models.CharField(max_length=20)
    correo_paciente = models.CharField(max_length=150)
    
    
    
