from rest_framework import serializers 
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    # traduccion de campos
    nombre_usuario = serializers.CharField(source='username')
    correo = serializers.EmailField(source='email')
    nombre = serializers.CharField(source='first_name')
    apellido = serializers.CharField(source='last_name')
    contrasena = serializers.CharField(
        source='password',  
        write_only=True,    #write_only por seguridad
        style={'input_type': 'password'}
    )

    class Meta:
        model = Usuario
        
        fields = [
            'id', 
            'nombre_usuario',  
            'correo',          
            'nombre',          
            'apellido',        
            'telefono',
            'rol',           
            'foto_perfil',   
            'foto_carnet',   
            'contrasena',      
        ]



