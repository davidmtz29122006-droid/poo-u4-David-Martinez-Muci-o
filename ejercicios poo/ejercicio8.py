def registrar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10.")
    print(f"Nota registrada: {nota}")

# Casos de prueba
try:
    registrar_nota(8.5)
    registrar_nota(12.0)
except ValueError as e:
    print(e)