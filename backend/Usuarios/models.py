from django.db import models

# usuarios/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Hereda username, password, email, first_name, last_name
    
    # Hacemos el email requerido y único (por defecto no lo es)
    email = models.EmailField(unique=True, blank=False, null=False) 

    ROLE_CHOICES = (
        ('solicitante', 'Solicitante'),
        ('repartidor', 'Repartidor'),
        ('ambos', 'Ambos'),
    )
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ambos')
    
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    # No es necesario __str__, AbstractUser ya lo define