# pedidos/serializers.py

from rest_framework import serializers
from .models import Pedidos
from usuario.models import Usuario  # Para mostrar info del cliente y repartidor

class PedidoSerializer(serializers.ModelSerializer):
    # Traducción y lectura de campos relacionados
    cliente_nombre = serializers.CharField(source='idCliente.username', read_only=True)
    repartidor_nombre = serializers.CharField(source='idRepartidor.username', read_only=True)

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
        ✅ SOLUCIÓN: Asigna automáticamente el usuario logueado como cliente
        """
        # Obtener el usuario de la request (viene del contexto)
        request = self.context.get('request')
        
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("Debes estar logueado para crear un pedido.")
        
        # Asignar el usuario logueado como cliente
        validated_data['idCliente'] = request.user
        
        # Crear el pedido
        pedido = Pedidos.objects.create(**validated_data)
        return pedido

    def update(self, instance, validated_data):
        
        #Actualiza un pedido existente.
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    #hola