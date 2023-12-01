from django.contrib import admin
from clinicaApp.models import Paciente, Doctor

# Register your models here. se crea cada clase por cada tabla que tenemos en DB
admin.site.register(Paciente)
admin.site.register(Doctor)