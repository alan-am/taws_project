#pedidos/models.py
from django.db import models
from usuario.models import Usuario #Estoy importando el modelo usuario por las relaciones que hay

# Create your models here.
class Pedidos(models.Model):
    codigoPedido= models.AutoField(primary_key=True)
    #relaciones
    idCliente= models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='pedidos_realizados')
    idRepartidor= models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos_entregados', null=True, blank=True)
   
    #info de contacto
    num_whats=models.CharField(max_length=12)
    descripcion= models.TextField()

    #Ubicaciones(texto directo)
    punto_origen_id= models.CharField(max_length=255) 
    punto_destino_id= models.CharField(max_length=255)

    #estado pedido
    estado= models.CharField(max_length=50, choices=[('Publicado', 'Publicado'), ('Aceptado', 'Aceptado')
                                                     , ('Entregado', 'Entregado')], default='Publicado')
    #Fechas y costo
    fechaInicial= models.DateTimeField(auto_now_add= True) #fecha creacion registro del pedido
    horaDeseada= models.DateTimeField(null=True, blank=True) #campo opcional  
    fechaFinal= models.DateTimeField(null= True, blank= True) #fecha de cierre del pedido
    costoEnvio= models.DecimalField(max_digits=5, decimal_places=2)

    #Atributos por si es impresion(son opcionales)
    archivo_pdf = models.URLField(max_length=500, null=True, blank=True)
    
    COLOR_CHOICES = [
        ('Blanco y Negro', 'Blanco y Negro'),
        ('Color', 'Color')
    ]
    formato_color = models.CharField(max_length=50, choices=COLOR_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.codigoPedido} - Cliente: {self.idCliente.username}"

