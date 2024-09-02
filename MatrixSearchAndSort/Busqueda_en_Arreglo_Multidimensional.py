# Definir la matriz bidimensional (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor_en_matriz(matriz, valor_a_buscar):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                return (i, j)  # Retorna la posición (fila, columna)
    return None

# Valor que queremos buscar en la matriz
valor = 5
resultado = buscar_valor_en_matriz(matriz, valor)

# Mostrar el resultado de la búsqueda
if resultado:
    print(f"Valor {valor} encontrado en la posición {resultado}")
else:
    print(f"Valor {valor} no encontrado en la matriz.")
