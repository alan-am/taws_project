#usuario/api.py
from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all(); #trae todos los registros
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        """
        AllowAny  para la acción creacion de usuarios(POST),
        IsAuthenticated' para todos los demás.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            # 'list', 'retrieve', 'update', 'delete'
            permission_classes = [permissions.IsAuthenticated]
            
        return [permission() for permission in permission_classes]