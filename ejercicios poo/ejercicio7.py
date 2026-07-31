def vender(inventario, medicamento, cantidad):
    stock_actual = inventario[medicamento]
    if cantidad > stock_actual:
        raise Exception("No hay suficiente stock disponible.")
    
    inventario[medicamento] -= cantidad
    print(f"Venta realizada. Nuevo stock de {medicamento}: {inventario[medicamento]}")

# Casos de prueba
mi_inventario = {"paracetamol": 50}

try:
    vender(mi_inventario, "paracetamol", 10)
    vender(mi_inventario, "paracetamol", 100)
except Exception as e:
    print(e)