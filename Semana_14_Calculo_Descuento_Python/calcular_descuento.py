def calcular_descuento(monto_total, porcentaje_descuento=25):
    """
    Calcula el monto del descuento a partir del monto total de la compra y el porcentaje de descuento.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar (default es 25).

    Retorna:
    float: El monto del descuento calculado.
    """
    # Calcula el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Programa principal
# Llamada a la función con monto total y porcentaje de descuento por defecto
monto1 = 1000  # Monto total de la compra
descuento1 = calcular_descuento(monto1)  # Descuento con 25%
monto_final1 = monto1 - descuento1  # Monto a pagar después del descuento
print(f"Monto total: {monto1}, Descuento: {descuento1}, Monto a pagar: {monto_final1}")

# Llamada a la función con monto total y un porcentaje de descuento específico
monto2 = 2000  # Monto total de la compra
porcentaje2 = 15  # Porcentaje de descuento
descuento2 = calcular_descuento(monto2, porcentaje2)  # Descuento con 15%
monto_final2 = monto2 - descuento2  # Monto a pagar después del descuento
print(f"Monto total: {monto2}, Descuento: {descuento2}, Monto a pagar: {monto_final2}")
