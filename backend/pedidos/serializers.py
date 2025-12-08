# pedidos/serializers.py

from rest_framework import serializers
from .models import Pedidos
from usuario.models import Usuario  # Para mostrar info del cliente y repartidor

class PedidoSerializer(serializers.ModelSerializer):
    # Traducción y lectura de campos relacionados
    cliente_nombre = serializers.CharField(source='idCliente.first_name', read_only=True)
    repartidor_nombre = serializers.CharField(source='idRepartidor.first_name', read_only=True)

    class Meta:
        model = Pedidos
        fields = [
            'codigoPedido',
            'idCliente',
            'cliente_nombre',
            'idRepartidor',
            'repartidor_nombre',
            'num_whats',
            'descripcion',
            'punto_origen',
            'punto_destino',
            'estado',
            'fechaInicial',
            'horaDeseada',
            'fechaFinal',
            'costoEnvio',
            'archivo_pdf',
            'formato_color',
            'codigo_entrega',
        ]
        read_only_fields = ['idCliente']
        #extra_kwargs = {
         #   'fechaFinal': {'required': False, 'allow_null': True},
         #   'idRepartidor': {'required': False, 'allow_null': True},
        #}

    def create(self, validated_data):
        """
        Crea y retorna un nuevo pedido, asignando el cliente del request.
        """
        # Obtener el usuario autenticado del contexto
        request = self.context.get('request')
        
        # Asignar el cliente automáticamente desde el usuario autenticado
        validated_data['idCliente'] = request.user
        
        # Crear y guardar el pedido
        instance = Pedidos(**validated_data)
        instance.save()
        
        return instance

    def update(self, instance, validated_data):
        
        #Actualiza un pedido existente.
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    #hola