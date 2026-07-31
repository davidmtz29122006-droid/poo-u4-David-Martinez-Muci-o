import sqlite3

class EspecieInvalidaError(Exception):
    """Excepción personalizada para cuando la especie no está permitida."""
    pass

class VeterinariaDB:
    def __init__(self, db_name="veterinaria.db"):
        self.db_name = db_name
        self.inicializar_base_datos()

    def inicializar_base_datos(self):
        """Crea la tabla de mascotas si no existe."""
        try:
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS mascotas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        especie TEXT NOT NULL,
                        edad INTEGER NOT NULL,
                        dueno TEXT NOT NULL
                    )
                """)
                conexion.commit()
        except sqlite3.Error as e:
            print(f"Error crítico al inicializar la base de datos: {e}")

    def registrar_mascota(self, nombre, especie, edad, dueno):
        """Registra una mascota validando los datos antes de guardarlos."""
        especies_permitidas = ["perro", "gato", "ave", "conejo"]
        
        try:
            # Validación de lógica de negocio (Excepción explícita)
            if especie.lower() not in especies_permitidas:
                raise EspecieInvalidaError(f"La especie '{especie}' no es atendida en esta clínica.")
            
            if not isinstance(edad, int) or edad < 0:
                raise ValueError("La edad debe ser un número entero positivo.")

            # Inserción en la base de datos (Excepción implícita de SQLite)
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                cursor.execute("""
                    INSERT INTO mascotas (nombre, especie, edad, dueno)
                    VALUES (?, ?, ?, ?)
                """, (nombre, especie.lower(), edad, dueno))
                conexion.commit()
                print(f"¡Éxito! Mascota '{nombre}' registrada correctamente.")

        except EspecieInvalidaError as e:
            print(f"Error de validación: {e}")
        except ValueError as e:
            print(f"Error de datos: {e}")
        except sqlite3.Error as e:
            print(f"Error en la base de datos al registrar: {e}")
        finally:
            print("Operación de registro finalizada.")

# --- PRUEBAS DE FUNCIONAMIENTO ---
if __name__ == "__main__":
    app_veterinaria = VeterinariaDB()

    print("--- CASO 1: Registro Exitoso ---")
    app_veterinaria.registrar_mascota("Max", "Perro", 3, "David Martinez")

    print("\n--- CASO 2: Error de Especie no Permitida (Excepción Personalizada) ---")
    app_veterinaria.registrar_mascota("Leonel", "Iguana", 2, "Karol")

    print("\n--- CASO 3: Error de Tipo de Dato (Edad Negativa) ---")
    app_veterinaria.registrar_mascota("Luna", "Gato", -1, "Jochis")