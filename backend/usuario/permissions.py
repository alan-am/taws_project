#usuario/permissions.py

from rest_framework import permissions

class IsAdminRol(permissions.BasePermission):
    #permiso solo para admins
    def has_permission(self, request, view):
        # El usuario debe estar autenticado
        # 2. su rol debe ser 'admin'
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'admin')