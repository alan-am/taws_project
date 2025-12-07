from pedidos.models import Pedidos

def calcular_ganancias_repartidor(id_repartidor):
    """
    Calcula la suma total de ganancias generadas por un repartidor.
    Solo se cuentan pedidos entregados.
    """

    pedidos_entregados = Pedidos.objects.filter(
        idRepartidor_id=id_repartidor,
        estado='Entregado'
    )

    total = sum([p.costoEnvio for p in pedidos_entregados])

    return float(total)