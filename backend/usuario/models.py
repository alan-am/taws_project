# usuario/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):

    # id, username, first_name, last_name, email, password ya estan en Abstract User(luego hacer un DTO )

    #Atributos EXTRAS
    telefono = models.CharField(max_length=20, blank=False, null= False)

    TIPOS_ROLES = (
        ('estudiante', 'Estudiante'),
        ('repartidor', 'Repartidor'),
    )
    rol = models.CharField(max_length=50, choices=TIPOS_ROLES, default='estudiante')
    foto_perfil = models.URLField(max_length=200, blank=False, null= False)
    foto_carnet = models.URLField(max_length=200, blank=False, null=False)

    #Configuraciones extras
    email = models.EmailField(unique=True, blank=False) #PK 


    #metodos
    def __str__(self):
        return self.username

