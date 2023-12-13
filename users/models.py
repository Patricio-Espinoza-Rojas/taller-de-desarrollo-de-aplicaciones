from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    access = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

