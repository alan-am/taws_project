from django.core.management.base import BaseCommand
from usuario.models import Usuario

class Command(BaseCommand):
    help = 'Carga usuarios iniciales de prueba en la db'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Iniciando carga de usuarios...')

        # -----------------------------------------------------------
        # USUARIO DE PRUEBA - estudiante
        #    Email: test@correo.com / Pass: 1234
        # -----------------------------------------------------------
        if not Usuario.objects.filter(email='test@correo.com').exists():
            Usuario.objects.create_user(
                username='test_user',
                email='test@correo.com',
                password='1234',
                first_name='Usuario',
                last_name='Prueba',
                rol='estudiante',
                telefono='0990000000'
            )
            self.stdout.write(self.style.SUCCESS(' - Estudiante Test creado (test@correo.com / 1234)'))

        # -----------------------------------------------------------
        # REPARTIDOR 1
        # -----------------------------------------------------------
        if not Usuario.objects.filter(email='marco@correo.com').exists():
            Usuario.objects.create_user(
                username='marco_r',
                email='marco@correo.com',
                password='123',
                first_name='Marco',
                last_name='Repartidor',
                rol='repartidor',
                telefono='0987654321'
            )
            self.stdout.write(self.style.SUCCESS(' - Repartidor 1 (Marco) creado'))

        # -----------------------------------------------------------
        #  REPARTIDOR 2
        # -----------------------------------------------------------
        if not Usuario.objects.filter(email='juan@correo.com').exists():
            Usuario.objects.create_user(
                username='juan_r',
                email='juan@correo.com',
                password='123',
                first_name='Juan',
                last_name='Veloz',
                rol='repartidor',
                telefono='0912345678'
            )
            self.stdout.write(self.style.SUCCESS(' - Repartidor 2 (Juan) creado'))

        self.stdout.write(self.style.SUCCESS('✅ Carga de usuarios completada.'))
