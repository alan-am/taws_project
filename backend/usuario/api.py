#usuario/api.py
from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

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
    

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        """
        Devuelve la información del usuario autenticado (dueño del token).
        """
        usuario = request.user
        
        # Usamos el serializer de la clase para convertir el usuario a JSON
        serializer = self.get_serializer(usuario)
        
        # Devolvemos el JSON para el front con todos los datos del usuario logueado.
        return Response(serializer.data)