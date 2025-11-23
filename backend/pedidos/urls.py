# pedidos/urls.py
from django.urls import path
from rest_framework import routers
from .api import PedidoViewSet


urlpatterns = [
    #Lista los pedidos que aun no han sido aceptados
    path(
        'api/pedido/publicados/',
        PedidoViewSet.as_view({'get': 'publicados'}),
        name='pedido-publicados'
    ),
    # Listar
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
]