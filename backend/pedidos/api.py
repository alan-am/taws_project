from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pedidos
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Al crear, asignamos al cliente automáticamente
    def perform_create(self, serializer):
        serializer.save(idCliente=self.request.user)

    # --- NUEVA LÓGICA: ACCIÓN PARA ACEPTAR PEDIDO ---
    @action(detail=True, methods=['patch'], url_path='aceptar')
    def aceptar_pedido(self, request, pk=None):
        pedido = self.get_object()
        
        # 1. Validar que nadie lo haya ganado antes
        if pedido.estado != 'Publicado':
             return Response({'error': 'Este pedido ya no está disponible.'}, status=status.HTTP_400_BAD_REQUEST)

        # 2. Asignar al repartidor actual (tú) y cambiar estado
        pedido.idRepartidor = request.user
        pedido.estado = 'Aceptado'
        pedido.save()
        
        # 3. Retornar el pedido actualizado
        serializer = self.get_serializer(pedido)
        return Response(serializer.data)
    @action(detail=True, methods=['post'], url_path='simular-aceptacion')
    def simular_aceptacion(self, request, pk=None):
        pedido = self.get_object()
        
        # 1. Buscamos (o creamos) al usuario ficticio
        # CORRECCIÓN: Usamos 'email' para buscar (es único) y los campos correctos de Django (first_name, last_name)
        from usuario.models import Usuario
        bot, created = Usuario.objects.get_or_create(
            email='flash@rapifavor.com', 
            defaults={
                'username': 'repartidor_flash',
                'first_name': 'Repartidor', # Antes 'nombre' (incorrecto en modelo)
                'last_name': 'Flash ⚡',   # Antes 'apellido' (incorrecto en modelo)
                'rol': 'repartidor',
            }
        )

        # Si se acabó de crear, le ponemos contraseña (opcional, por si quieres loguearte con él)
        if created:
            bot.set_password('bot123')
            bot.save()
        
        # 2. Le asignamos el pedido
        pedido.idRepartidor = bot
        pedido.estado = 'Aceptado'
        pedido.save()
        
        return Response({'status': 'Pedido aceptado por Repartidor Flash'})
    @action(detail=True, methods=['post'], url_path='simular-entrega')
    def simular_entrega(self, request, pk=None):
        pedido = self.get_object()
        
        # Verificamos que sea nuestro bot quien lo tiene
        if pedido.idRepartidor and pedido.idRepartidor.username == 'repartidor_flash':
             pedido.estado = 'Entregado'
             pedido.save()
             return Response({'status': 'Pedido entregado por Repartidor Flash 📦'})
        
        return Response({'error': 'Este pedido no lo tiene el bot'}, status=status.HTTP_400_BAD_REQUEST)