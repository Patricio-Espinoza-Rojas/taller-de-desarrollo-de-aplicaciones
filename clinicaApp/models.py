from django.db import models

# Create your models here.
#para tambien tener los aprametros con sql
class Project (models.Model):#tabla llamada project
    name = models.CharField(max_length=200)
    
    
