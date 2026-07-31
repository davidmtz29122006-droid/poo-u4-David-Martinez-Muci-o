def sumar(a, b):
    try:
        return a + b
    except TypeError:
        print("No se pueden sumar tipos de datos diferentes (ej. número y texto).")

# Casos de prueba
print(sumar(5, 10))
sumar(5, "10")