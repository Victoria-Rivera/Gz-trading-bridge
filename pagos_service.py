def calcular_totales(monto_neto):
    """Calcula el IVA (19%) sobre el total acumulado del carrito dinámico."""
    iva = int(monto_neto * 0.19)
    total_con_iva = monto_neto + iva
    return iva, total_con_iva