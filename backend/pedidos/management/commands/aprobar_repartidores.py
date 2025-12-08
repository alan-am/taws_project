# backend/pedidos/management/commands/aprobar_repartidores.py
from django.core.management.base import BaseCommand
from usuario.models import Usuario

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Usuario.objects.filter(rol='repartidor', estado_verificacion='Pendiente').update(
            estado_verificacion='Aprobado'
        )
        print("✅ Todos los repartidores aprobados")