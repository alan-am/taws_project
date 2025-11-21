# usuario/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):

    # id, username, first_name, last_name, email, password ya estan en Abstract User
    username = models.CharField(
        max_length=150,
        unique=False,  # No PK
        blank=True,    # opcional
        null=True      # y puede ser nulo
    )

    TIPOS_ROLES = (
        ('estudiante', 'Estudiante'),
        ('repartidor', 'Repartidor'),
    )
    rol = models.CharField(max_length=50, choices=TIPOS_ROLES, default='estudiante')

    #Campos extras - opcionales
    telefono = models.CharField(max_length=20, blank=True, null= True)
    foto_perfil = models.URLField(max_length=200, blank=True, null= True)
    foto_carnet = models.URLField(max_length=200, blank=True, null=True)

    #Configuraciones extras
    email = models.EmailField(unique=True, blank=False) #PK 

    #Config del login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #metodos
    def __str__(self):
        return self.email

