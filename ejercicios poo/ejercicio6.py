def registrar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    print(f"Edad registrada: {edad}")

# Casos de prueba
try:
    registrar_edad(25)
    registrar_edad(-5)
except ValueError as e:
    print(e)