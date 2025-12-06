# usuario/serializers.py

from rest_framework import serializers 
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    # traduccion de campos
    nombre_usuario = serializers.CharField(source='username', required=False, allow_blank=True) #lo sobreescribimos como opcional


    #
    correo = serializers.EmailField(source='email')
    nombre = serializers.CharField(source='first_name', required=True)
    apellido = serializers.CharField(source='last_name', required=True)
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
            'estado_verificacion'   
        ]
        #verificacion en solo lectura
        read_only_fields = ['estado_verificacion'] 
    def create(self, validated_data):
        """
        Crea y retorna un nuevo usuario, hasheando la contraseña.
        """
        # Sacamos el password del diccionario de datos validados
        password = validated_data.pop('password', None)
        
        # Creamos el usuario con el resto de los datos
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            # set_password() se encarga de hashear la contraseña
            instance.set_password(password)
            
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        Actualiza un usuario, hasheando la contraseña si se provee una nueva.
        """
        password = validated_data.pop('password', None)
        
        # Llama al 'update' normal del padre para los campos comunes
        instance = super().update(instance, validated_data)

        if password is not None:
            # hashear password nuevo
            instance.set_password(password)
            instance.save()
            
        return instance


# Serializer simple solo para recibir la imagen
class ImagenUploadSerializer(serializers.Serializer):
    imagen = serializers.ImageField()
    tipo = serializers.ChoiceField(choices=[('perfil', 'Foto de Perfil'), ('carnet', 'Foto de Carnet')])

