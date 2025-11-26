from django.urls import path
from rest_framework import routers
from .api import PedidoViewSet

router = routers.DefaultRouter()
router.register('api/pedido', PedidoViewSet, "pedido")  # CRUD automático

urlpatterns = [
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
    path('api/pedido/aceptar/<int:pk>/', PedidoViewSet.as_view({'patch': 'aceptar_pedido'}), name='pedido-aceptar'),
    path('api/pedido/simular-aceptacion/<int:pk>/', PedidoViewSet.as_view({'post': 'simular_aceptacion'}), name='simular-aceptacion'),
    path('api/pedido/simular-entrega/<int:pk>/', PedidoViewSet.as_view({'post': 'simular_entrega'}), name='simular-entrega'),
]
