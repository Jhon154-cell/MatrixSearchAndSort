# Definir la matriz bidimensional (3x3)
matriz = [
    [9, 3, 5],
    [2, 8, 7],
    [6, 4, 1]
]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    # Algoritmo de ordenación Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la segunda fila ordenada:")
for fila in matriz:
    print(fila)
