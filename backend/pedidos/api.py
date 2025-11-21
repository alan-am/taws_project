from rest_framework import viewsets, permissions
from .models import Pedidos
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer
    
    # 1. Obligamos a que solo usuarios logueados puedan pedir
    permission_classes = [permissions.IsAuthenticated]

    # 2. ESTA ES LA MAGIA:
    # Al crear un pedido, inyectamos automáticamente al usuario logueado como 'idCliente'
    def perform_create(self, serializer):
        serializer.save(idCliente=self.request.user)