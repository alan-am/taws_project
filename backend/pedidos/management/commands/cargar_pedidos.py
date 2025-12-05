#pedidos/cargar_pedidos.py
from django.core.management.base import BaseCommand
from pedidos.models import Pedidos
from usuario.models import Usuario
from django.utils import timezone

class Command(BaseCommand):
    help = 'Carga pedidos iniciales de prueba en la db'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Iniciando carga de pedidos...')

        # -----------------------------------------------------------
        # Verificar usuarios necesarios
        # -----------------------------------------------------------
        try:
            cliente = Usuario.objects.get(username='test_user')
            repartidor_1 = Usuario.objects.get(username='marco_r')
            repartidor_2 = Usuario.objects.get(username='juan_r')
        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(
                "ERROR: Faltan usuarios de prueba. Ejecuta antes: python manage.py cargar_usuarios"
            ))
            return

        # -----------------------------------------------------------
        # Pedido 1 (Publicado, sin repartidor)
        # -----------------------------------------------------------
        if not Pedidos.objects.filter(descripcion='Pedido de prueba 1').exists():
            Pedidos.objects.create(
                idCliente=cliente,
                idRepartidor=None,
                num_whats='0991111111',
                descripcion='Pedido de prueba 1',
                punto_origen='FCNM - Biblioteca',
                punto_destino='FIEC - Bloque 11',
                estado='Publicado',
                horaDeseada=timezone.now() + timezone.timedelta(hours=1),
                costoEnvio=1.50,
                archivo_pdf=None,
                formato_color=None
            )
            self.stdout.write(self.style.SUCCESS(' - Pedido 1 creado (Publicado)'))

        # -----------------------------------------------------------
        # Pedido 2 (Publicado, sin repartidor)
        # -----------------------------------------------------------
        if not Pedidos.objects.filter(descripcion='Pedido de prueba 2').exists():
            Pedidos.objects.create(
                idCliente=cliente,
                idRepartidor=None,
                num_whats='0992222222',
                descripcion='Pedido de prueba 2',
                punto_origen='FADCOM - Entrada',
                punto_destino='FCSH - Laboratorios',
                estado='Publicado',
                horaDeseada=timezone.now() + timezone.timedelta(hours=2),
                costoEnvio=2.00,
                archivo_pdf=None,
                formato_color='Color'
            )
            self.stdout.write(self.style.SUCCESS(' - Pedido 2 creado (Publicado)'))

        # -----------------------------------------------------------
        # Pedido 3 (Entregado por Juan)
        # -----------------------------------------------------------
        if not Pedidos.objects.filter(descripcion='Pedido de prueba 3').exists():
            Pedidos.objects.create(
                idCliente=cliente,
                idRepartidor=repartidor_2,
                num_whats='0993333333',
                descripcion='Pedido de prueba 3',
                punto_origen='FIEC - Cafetería',
                punto_destino='FCSH - Aula 003',
                estado='Entregado',
                fechaFinal=timezone.now(),
                horaDeseada=timezone.now(),
                costoEnvio=1.25,
                archivo_pdf='https://example.com/archivo.pdf',
                formato_color='Blanco y Negro'
            )
            self.stdout.write(self.style.SUCCESS(' - Pedido 3 creado (Entregado por Juan)'))

        self.stdout.write(self.style.SUCCESS('✅ Carga de pedidos completada.'))