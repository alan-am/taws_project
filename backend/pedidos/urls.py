# pedidos/urls.py
from django.urls import path
from rest_framework import routers
from .api import PedidoViewSet
from .api import PedidoViewSet, GananciasRepartidorView

router = routers.DefaultRouter()
router.register('crear', PedidoViewSet, 'pedidos')



urlpatterns = [
    #Lista los pedidos que aun no han sido aceptados
    path(
        'api/pedido/publicados/',
        PedidoViewSet.as_view({'get': 'publicados'}),
        name='pedido-publicados'
    ),
    #Endpoints codigo OTP - flujo de entrega
    # Aceptar Pedido (Genera OTP), lleva el id del pedido aceptado en la ruta
    path(
        'api/pedido/aceptar/<int:pk>/',
        PedidoViewSet.as_view({'patch': 'aceptar_pedido'}),
        name='pedido-aceptar'
    ),
    # Finalizar Entrega (Valida OTP)
    # POST /api/pedido/finalizar/1/  Body: { "otp": "xxxx" }
    path(
        'api/pedido/finalizar/<int:pk>/',
        PedidoViewSet.as_view({'post': 'finalizar_entrega'}),
        name='pedido-finalizar'
    ),


    # endpoitns CRUD
    #listar
    path(
        'api/pedido/listar/',
        PedidoViewSet.as_view({'get': 'list'}),
        name='pedido-listar'
    ),
    
    # Crear
    path(
        'api/pedido/crear/',
        PedidoViewSet.as_view({'post': 'create'}),
        name='pedido-crear'
    ),
    
    # Detalle
    path(
        'api/pedido/detalle/<int:pk>/',
        PedidoViewSet.as_view({'get': 'retrieve'}),
        name='pedido-detalle'
    ),
    
    # Actualizar
    path(
        'api/pedido/actualizar/<int:pk>/',
        PedidoViewSet.as_view({'put': 'update', 'patch': 'partial_update'}),
        name='pedido-actualizar'
    ),
    
    # Eliminar
    path(
        'api/pedido/eliminar/<int:pk>/',
        PedidoViewSet.as_view({'delete': 'destroy'}),
        name='pedido-eliminar'
    ),
    path(
            'api/pedido/ganancias/', 
            PedidoViewSet.as_view({'get': 'ganancias'}), 
            name='ganancias-repartidor'
        ),

    path(
        'api/pedido/precio_dinamico/',
        PedidoViewSet.as_view({'get': 'precio_dinamico'}),
        name='pedido-precio-dinamico'
    ),
    
    # También falta esta para ganancias:
    path(
        'api/pedido/ganancias/',
        PedidoViewSet.as_view({'get': 'ganancias'}),
        name='pedido-ganancias'
    ),

]