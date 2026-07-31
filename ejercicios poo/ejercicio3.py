def buscar_medicamento(medicamento):
    inventario = {"paracetamol": 50, "ibuprofeno": 20}
    try:
        return inventario[medicamento]
    except KeyError:
        print(f"El medicamento '{medicamento}' no está registrado.")

# Casos de prueba
print(buscar_medicamento("paracetamol"))
buscar_medicamento("aspirina")