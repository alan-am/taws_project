from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all(); #trae todos los registros
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer