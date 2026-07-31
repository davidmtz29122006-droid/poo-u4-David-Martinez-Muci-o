def obtener_color(indice):
    colores = ["rojo", "verde", "azul"]
    try:
        return colores[indice]
    except IndexError:
        print(f"Ese índice no existe. Solo hay {len(colores)} colores disponibles.")

# Casos de prueba
print(obtener_color(1))
obtener_color(5)