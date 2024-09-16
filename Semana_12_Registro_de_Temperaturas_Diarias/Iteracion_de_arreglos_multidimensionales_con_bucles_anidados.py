# Definir las dimensiones de la matriz
ciudades = ['Ciudad1', 'Ciudad2', 'Ciudad3']  # 3 ciudades
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']  # 7 días
semanas = 2  # 2 semanas

# Inicializar la matriz 3D con datos de ejemplo (temperaturas aleatorias)
# La matriz tiene [número de ciudades][días de la semana][número de semanas]
temperaturas = [
    [[25, 27], [26, 28], [30, 29], [32, 31], [28, 30], [29, 27], [26, 25]],  # Ciudad1
    [[20, 22], [21, 23], [22, 24], [23, 25], [24, 26], [25, 27], [26, 28]],  # Ciudad2
    [[15, 17], [16, 18], [17, 19], [18, 20], [19, 21], [20, 22], [21, 23]]  # Ciudad3
]

# Calcular el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")

    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[i][dia][semana]

        promedio_semana = suma_temperaturas / len(dias_semana)
        print(f"Semana {semana + 1}: {promedio_semana:.2f}°C")
