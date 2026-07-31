class StockInsuficienteError(Exception):
    pass

def vender_con_error_propio(inventario, medicamento, cantidad):
    stock_actual = inventario[medicamento]
    if cantidad > stock_actual:
        faltante = cantidad - stock_actual
        raise StockInsuficienteError(f"Faltan {faltante} unidades de {medicamento}.")
    
    inventario[medicamento] -= cantidad
    print(f"Venta exitosa. Stock: {inventario[medicamento]}")

# Casos de prueba
mi_inventario = {"ibuprofeno": 20}

try:
    vender_con_error_propio(mi_inventario, "ibuprofeno", 5)
    vender_con_error_propio(mi_inventario, "ibuprofeno", 30)
except StockInsuficienteError as e:
    print(e)