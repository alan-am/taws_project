#usuario/api.py
from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsAdminRol

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

        elif self.action in ['pendientes', 'gestionar_verificacion']:
            # Solo el ADMIN puede ver pendientes o aprobar gente
            permission_classes = [IsAdminRol]
        else:
            # Para lo demás (listar, perfil, editar), usuario logueado
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
    
    # ENDPOINT: Listar usuarios pendientes (solo Admins) ---
    @action(detail=False, methods=['get'], url_path='pendientes')
    def pendientes(self, request):
        """
        Retorna usuarios que aún no han sido verificados.
        """
        # Filtramos solo los que tienen estado 'Pendiente'
        usuarios_pendientes = Usuario.objects.filter(estado_verificacion='Pendiente')
        serializer = self.get_serializer(usuarios_pendientes, many=True)
        return Response(serializer.data)

    # ENDPOINT: Aprobar/Rechazar Usuario (Solo Admin) ---
    @action(detail=True, methods=['patch'], url_path='verificar')
    def gestionar_verificacion(self, request, pk=None):
        """
        Permite al admin cambiar el estado a 'Aprobado' o 'Rechazado'.
        Body esperado: { "estado": "Aprobado" }
        """
        usuario = self.get_object() # Obtiene el usuario por ID (pk)
        nuevo_estado = request.data.get('estado')

        if nuevo_estado not in ['Aprobado', 'Rechazado', 'Pendiente']:
            return Response(
                {'error': 'Estado no válido. Use: Aprobado, Rechazado o Pendiente'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        usuario.estado_verificacion = nuevo_estado
        usuario.save()

        return Response({
            'mensaje': f'Usuario {usuario.email} actualizado exitosamente.',
            'nuevo_estado': usuario.estado_verificacion
        })