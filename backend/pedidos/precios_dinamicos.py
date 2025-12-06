# pedidos/precios_dinamicos.py
import math

def calcular_precio_dinamico(distancia_km, tipo_favor):
    """
    Calcula el precio dinámico del envío basándose en:
    - distancia del envío (km)
    - tipo de favor (normal, urgente, pesado)
    - tarifa base
    """

    # Tarifa base mínima
    TARIFA_BASE = 1.00  

    # Costo por km
    COSTO_POR_KM = 0.40  

    # Multiplicadores según tipo de favor
    MULTIPLICADORES = {
        'normal': 1.0,
        'urgente': 1.3,
        'pesado': 1.5
    }

    if tipo_favor not in MULTIPLICADORES:
        raise ValueError("Tipo de favor inválido. Usa: normal, urgente o pesado.")

    # Cálculo del costo
    costo_distancia = distancia_km * COSTO_POR_KM
    costo_final = (TARIFA_BASE + costo_distancia) * MULTIPLICADORES[tipo_favor]

    # redondeo
    return round(costo_final, 2)