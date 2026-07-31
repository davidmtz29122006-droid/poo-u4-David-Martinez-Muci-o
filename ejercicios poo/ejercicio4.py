def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        print(f"Tu edad es: {edad}")
    except ValueError:
        print("Error: Debes escribir un número entero.")

# Caso de prueba
pedir_edad()