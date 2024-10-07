# Escritura de Archivo de Texto
# Creamos el archivo 'my_notes.txt' en modo de escritura ('w') y escribimos 8 líneas de notas.
with open('my_notes.txt', 'w') as file:
    file.write("Hoy comencé a aprender sobre la manipulación de archivos en Python.\n")
    file.write("Es fascinante cómo puedo escribir y leer archivos de texto fácilmente.\n")
    file.write("Entiendo que es importante cerrar los archivos después de usarlos.\n")
    file.write("Python facilita este proceso con la declaración 'with'.\n")
    file.write("Me siento más cómodo con la sintaxis de Python.\n")
    file.write("Hoy también practiqué estructuras de control y bucles en Python.\n")
    file.write("Cada día estoy más seguro en mis habilidades de programación.\n")
    file.write("Voy a seguir practicando para mejorar mis habilidades aún más.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo de lectura ('r') y leemos línea por línea.
with open('my_notes.txt', 'r') as file:
    line = file.readline()  # Leemos la primera línea
    while line:
        print(line.strip())  # Imprimimos la línea eliminando los saltos de línea adicionales
        line = file.readline()  # Leemos la siguiente línea

# No es necesario cerrar el archivo manualmente porque 'with' lo hace automáticamente al finalizar el bloque
