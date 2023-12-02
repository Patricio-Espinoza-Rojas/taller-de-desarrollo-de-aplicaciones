from django.db import models

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_especialidad

class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    dia = models.DateTimeField()
    hora = models.DateTimeField()

    def __str__(self):
        return f"{self.dia} - {self.hora}"

class Tipousuario(models.Model):
    id_tipousuario = models.AutoField(primary_key=True)
    nombre_tipousuario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_tipousuario

class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_permiso

class Medicamentos(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=100)
    gramos = models.FloatField()

    def __str__(self):
        return f"{self.nombre_medicamento} - {self.gramos}"

class Paciente(models.Model):
    rut_paciente = models.CharField(max_length=13, primary_key=True)
    nombre_paciente = models.CharField(max_length=150)
    direccion_paciente = models.CharField(max_length=200)
    telefono_paciente = models.CharField(max_length=20)
    correo_paciente = models.CharField(max_length=150)
    tipousuario = models.ForeignKey(Tipousuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.rut_paciente} - {self.nombre_paciente}"

class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    nombre_doctor = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, default=1)
    correo = models.CharField(max_length=150)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, default=1)
    foto = models.ImageField(upload_to='doctores/', null=True, blank=True)
    tipousuario = models.ForeignKey(Tipousuario, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"{self.nombre_doctor} - {self.especialidad} - {self.agenda}"

class FichaPaciente(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    anamnesis = models.CharField(max_length=100)
    diagnostico = models.IntegerField()
    fecha = models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=1)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, default=1)
    receta = models.ForeignKey('Receta', on_delete=models.CASCADE, default=1)

class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    medicamentos = models.ForeignKey(Medicamentos, on_delete=models.CASCADE, default=1)
    rutPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=1)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.rutPaciente} - {self.fecha} - {self.medicamentos} - {self.doctor}"
