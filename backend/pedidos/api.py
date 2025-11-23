# pedidos/api.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pedidos
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated] # Protegemos los pedidos

    @action(detail=False, methods=['get'])
    def publicados(self, request):
        """
        Retorna solo los pedidos con estado 'Publicado',
        ordenados desde el más reciente.
        """
        #Filtramos por estado 'Publicado' y en orden ascendente de fecha de creacion
        pedidos = Pedidos.objects.filter(estado='Publicado').order_by('-fechaInicial')

        serializer = self.get_serializer(pedidos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)