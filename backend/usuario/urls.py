#usuario/urls.py
from django.urls import path
from rest_framework import routers
from .api import UsuarioViewSet

router = routers.DefaultRouter() 


router.register('api/usuario', UsuarioViewSet, "usuario") #crear el crud

urlpatterns = [
    path(
        'api/usuario/me/', 
        UsuarioViewSet.as_view({'get': 'me'}), 
        name='usuario-me'
    ),
    # Listar (GET)
    path(
        'api/usuario/listar/', 
        UsuarioViewSet.as_view({'get': 'list'}), 
        name='usuario-listar'
    ),
    
    # Crear (POST)
    path(
        'api/usuario/crear/', 
        UsuarioViewSet.as_view({'post': 'create'}), 
        name='usuario-crear'
    ),
    
    # --- CRUD --

    #Detalle (GET /api/usuario/detalle/1/)
    path(
        'api/usuario/detalle/<int:pk>/', 
        UsuarioViewSet.as_view({'get': 'retrieve'}), 
        name='usuario-detalle'
    ),
    
    #Actualizar (PUT o PATCH /api/usuario/actualizar/1/)
    path(
        'api/usuario/actualizar/<int:pk>/', 
        UsuarioViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), 
        name='usuario-actualizar'
    ),
    
    #Eliminar (DELETE /api/usuario/eliminar/1/)
    path(
        'api/usuario/eliminar/<int:pk>/', 
        UsuarioViewSet.as_view({'delete': 'destroy'}), 
        name='usuario-eliminar'
    ),
    path(
        'api/usuario/subir-imagen/', 
        UsuarioViewSet.as_view({'post': 'subir_imagen'}), 
        name='usuario-subir-imagen'
    ),
]