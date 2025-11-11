#pedidos/models.py
from django.db import models
from usuario.models import Usuario #Estoy importando el modelo usuario por las relaciones que hay

# Create your models here.
class Pedidos(models.Model):
    codigoPedido= models.AutoField(primary_key=True)
    idCliente= models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='pedidos_realizados')
    idRepartidor= models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos_entregados', null=True, blank=True)
    num_whats=models.CharField(max_length=12)
    descripcion= models.TextField()
    punto_origen_id= models.IntegerField() #Despues habra que cambiarlo para relacionarlo con facultad
    punto_desitno_id= models.IntegerField() #Despues habra que cambiarlo para relacionarlo con facultad
    estado= models.CharField(max_length=50, choices=[('Publicado', 'Publicado'), ('Aceptado', 'Aceptado')
                                                     , ('Entregado', 'Entregado')])
    fechaInicial= models.DateTimeField()
    horaDeseada= models.DateTimeField()
    fechaFinal= models.DateTimeField(null= True, blank= True)
    costoEnvio= models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.codigoPedido} - Cliente: {self.idCliente.username}"

