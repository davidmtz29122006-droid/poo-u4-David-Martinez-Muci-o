def dividir_seguro(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")

# Casos de prueba
print(dividir_seguro(10, 2))
dividir_seguro(10, 0)