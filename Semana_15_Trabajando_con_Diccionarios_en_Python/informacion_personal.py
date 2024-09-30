# 1. Crear un diccionario llamado informacion_personal con claves como "nombre", "edad", "ciudad" y "profesion".
informacion_personal = {
    "nombre": "Juan Pérez",  # Nombre de la persona
    "edad": 30,              # Edad de la persona
    "ciudad": "Madrid",       # Ciudad donde vive la persona
    "profesion": "Ingeniero"  # Profesión de la persona
}

# 2. Acceder al valor asociado con la clave "ciudad" y modificarlo.
# Cambiamos la ciudad de "Madrid" a "Barcelona".
informacion_personal["ciudad"] = "Barcelona"

# 3. Agregar una nueva clave-valor al diccionario para representar la "profesion" de la persona.
# La clave "profesion" ya existe, pero cambiamos el valor a "Arquitecto".
informacion_personal["profesion"] = "Arquitecto"

# 4. Verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla.
# Usamos una condición para verificar si "telefono" no está en el diccionario.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "555-123456"  # Si no existe, se agrega un número ficticio.

# 5. Eliminar la clave "edad" del diccionario.
# Utilizamos el método pop() para eliminar la clave "edad".
# El segundo argumento 'None' evita un error si la clave no existe.
informacion_personal.pop("edad", None)

# 6. Imprimir el diccionario resultante.
# Mostramos el diccionario final después de todas las modificaciones.
print("Diccionario final:")
print(informacion_personal)
