def calcular_totales(monto_neto):
    """Calcula el IVA (19%) sobre el total acumulado del carrito dinámico."""
    iva = int(monto_neto * 0.19)
    total_con_iva = monto_neto + iva
    return iva, total_con_iva

def procesar_transaccion(metodo_pago, total_final):
    print(f" Conectando de forma segura con la pasarela ({metodo_pago})...")
    print(f"Procesando cargo financiero por ${total_final:,}".replace(",", "."))
    return True

def formatear_dinero(valor):
    return f"${valor:,.0f}".replace(",", ".")