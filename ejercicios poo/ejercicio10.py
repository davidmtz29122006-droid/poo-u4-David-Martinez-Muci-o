def validar_correo(correo):
    if "@" not in correo:
        raise ValueError("El correo electrónico no es válido porque le falta el '@'.")
    print("Correo verificado correctamente.")

# Casos de prueba
try:
    validar_correo("usuario@correo.com")
    validar_correo("usuariocorreo.com")
except ValueError as e:
    print(e)