from django.db import models

# Create your models here.
#para tambien tener los aprametros con sql
class Paciente(models.Model):#tabla llamada paciente
    #se crearon las tablas falta makemigracionts
    rut_paciente = models.CharField(max_length=13)
    nombre_paciente = models.CharField(max_length=150)
    direccion_paciente = models.CharField(max_length=200)
    telefono_paciente = models.CharField(max_length=20)
    correo_paciente = models.CharField(max_length=150)
    
class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre_especialidad

class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    nombre_doctor = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, default=1)
    correo = models.CharField(max_length=150)
    id_agenda = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='doctores/', null=True, blank=True)  

    
class Agenda(models.Model):

    id_agenda =models.IntegerField()
    dia = models.DateTimeField()
    hora = models.DateTimeField()

class FichaPaciente(models.Model):
    id_ficha = models.IntegerField()
    anamnesis = models.CharField(max_length=100)
    diagnostico = models.IntegerField()
    fecha = models.DateTimeField()
    rut_paciente = models.CharField(max_length=100)
    id_doctor = models.IntegerField(default=0)
    id_especialidad = models.IntegerField(default=0)
    id_receta = models.IntegerField()

class Receta(models.Model):
    id_receta = models.IntegerField()
    medicamentos = models.CharField(max_length=100)
    fecha = models.DateTimeField() 
    rutPaciente = models.CharField(max_length=10)
    id_doctor = models.IntegerField()
    
class Medicamentos(models.Model):
    id_medicamento = models.IntegerField()
    nombre_medicamento = models.CharField(max_length=100)
    gramos = models.FloatField()
    
class Tipousuario(models.Model):
    id_tipousuario = models.IntegerField()
    nombre_tipousuario = models.CharField(max_length=100)

class Permiso(models.Model):
    id_permiso = models.IntegerField()
    nombre_permiso = models.CharField(max_length=100)
    