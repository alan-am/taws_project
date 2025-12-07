# pedidos/api.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pedidos
from .serializers import PedidoSerializer
from django.utils import timezone
import random

from pedidos.precios_dinamicos import calcular_precio_dinamico
from pedidos.metricas_financieras import calcular_ganancias_repartidor

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
    
    # Metodo para aceptar pedido, que genera el codigo OTP
    @action(detail=True, methods=['patch'])
    def aceptar_pedido(self, request, pk=None):
        """
        El repartidor acepta el pedido. Se genera un PIN único de 4 dígitos.
        """
        pedido = self.get_object()
        usuario_actual = request.user

        # Validaciones
        if pedido.estado != 'Publicado':
            return Response(
                {'error': 'Este pedido ya no está disponible.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if usuario_actual.rol != 'repartidor':
             return Response(
                {'error': 'Solo los repartidores pueden aceptar pedidos.'}, 
                status=status.HTTP_403_FORBIDDEN
            )

        # 1. Asignar Repartidor
        pedido.idRepartidor = usuario_actual
        pedido.estado = 'Aceptado'

        # 2. Generar PIN de 4 dígitos (1000 a 9999)
        pin_generado = str(random.randint(1000, 9999))
        pedido.codigo_entrega = pin_generado
        
        pedido.save()

        # Retornamos el pedido (el cliente podrá ver el PIN en su historial)
        serializer = self.get_serializer(pedido)
        return Response({
            'mensaje': 'Pedido aceptado correctamente.',
            'pedido': serializer.data
        }, status=status.HTTP_200_OK)
    
     # Metodo para finalizar pedido, validando el codigo otp
    @action(detail=True, methods=['post'])
    def finalizar_entrega(self, request, pk=None):
        """
        El repartidor envía el PIN que le dio el cliente para finalizar.
        Body: { "otp": "1234" }
        """
        pedido = self.get_object()
        otp_ingresado = request.data.get('otp')

        # Validaciones previas
        if pedido.estado != 'Aceptado':
             return Response(
                {'error': 'El pedido debe estar en curso (Aceptado) para poder finalizarlo.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if not otp_ingresado:
            return Response(
                {'error': 'El código OTP es obligatorio.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # validacion codigo otp igual al de la db
        if otp_ingresado == pedido.codigo_entrega:
            # Éxito: Cerrar pedido
            pedido.estado = 'Entregado'
            pedido.fechaFinal = timezone.now()
            pedido.save()

            return Response({
                'mensaje': 'Código correcto, Entrega finalizada exitosamente.',
                'estado': 'Entregado'
            }, status=status.HTTP_200_OK)
        else:
            # Fallo
            return Response(
                {'error': 'Código incorrecto. Pídale al cliente que verifique el codigo.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        



     #  ENDPOINT: Calcular PRECIO DINÁMICO
    # ------------------------------------------------------------
    @action(detail=False, methods=['get'])
    def precio_dinamico(self, request):
        """
        Calcula el precio dinámico:
        /api/pedidos/precio_dinamico/?distancia=3.5&tipo=urgente
        """
        distancia = request.query_params.get('distancia')
        tipo = request.query_params.get('tipo')

        if not distancia or not tipo:
            return Response(
                {'error': 'Debe enviar los parámetros: distancia y tipo.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            distancia = float(distancia)
            precio = calcular_precio_dinamico(distancia, tipo)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {'distancia_km': distancia, 'tipo': tipo, 'precio': precio},
            status=status.HTTP_200_OK
        )

    # ------------------------------------------------------------
    #  ENDPOINT: GANANCIAS por repartidor
    # ------------------------------------------------------------
    @action(detail=False, methods=['get'])
    def ganancias(self, request):
        """
        Retorna el total de ganancias de un repartidor.
        Usa request.user para identificarlo.
        """
        usuario = request.user

        if usuario.rol != 'repartidor':
            return Response(
                {'error': 'Solo los repartidores pueden ver sus ganancias.'},
                status=status.HTTP_403_FORBIDDEN
            )

        total = calcular_ganancias_repartidor(usuario.id)

        return Response(
            {
                'repartidor': usuario.username,
                'ganancias_acumuladas': total
            },
            status=status.HTTP_200_OK
        )
    

    # --- AGREGA ESTO AL FINAL DE backend/pedidos/api.py ---

# Importaciones necesarias para la nueva vista
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class GananciasRepartidorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Aquí conectaremos la lógica real más adelante.
        # Por ahora devolvemos 0 para que el Dashboard funcione.
        return Response({
            "ganancias_acumuladas": 0.0,
            "pedidos_completados": 0
        })