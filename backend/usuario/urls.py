#usuario/urls.py
from rest_framework import routers
from .api import UsuarioViewSet

router = routers.DefaultRouter() 


router.register('api/usuario', UsuarioViewSet, "usuario") #crear el crud

urlpatterns = router.urls