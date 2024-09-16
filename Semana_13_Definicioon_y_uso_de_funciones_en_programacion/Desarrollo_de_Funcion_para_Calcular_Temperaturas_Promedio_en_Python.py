def calcular_promedio_temperaturas(temperaturas, ciudades, dias_semana, semanas):
    """
    Esta función calcula el promedio de temperaturas para cada ciudad
    en un período de tiempo dado (días de la semana y semanas).

    :param temperaturas: Lista 3D con datos de temperaturas [ciudad][día][semana].
    :param ciudades: Lista con nombres de las ciudades.
    :param dias_semana: Lista con los nombres de los días de la semana.
    :param semanas: Número total de semanas.

    :return: None. Muestra los promedios en pantalla.
    """
    for i, ciudad in enumerate(ciudades):
        print(f"\nPromedios de temperatura para {ciudad}:")

        for semana in range(semanas):
            suma_temperaturas = 0
            for dia in range(len(dias_semana)):
                suma_temperaturas += temperaturas[i][dia][semana]

            promedio_semana = suma_temperaturas / len(dias_semana)
            print(f"Semana {semana + 1}: {promedio_semana:.2f}°C")


# Ejemplo de uso con datos
ciudades = ['Ciudad1', 'Ciudad2', 'Ciudad3']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

temperaturas = [
    [[25, 27, 26, 28], [26, 28, 27, 29], [30, 29, 28, 30], [32, 31, 30, 32], [28, 30, 29, 31], [29, 27, 28, 30],
     [26, 25, 27, 29]],  # Ciudad1
    [[20, 22, 21, 23], [21, 23, 22, 24], [22, 24, 23, 25], [23, 25, 24, 26], [24, 26, 25, 27], [25, 27, 26, 28],
     [26, 28, 27, 29]],  # Ciudad2
    [[15, 17, 16, 18], [16, 18, 17, 19], [17, 19, 18, 20], [18, 20, 19, 21], [19, 21, 20, 22], [20, 22, 21, 23],
     [21, 23, 22, 24]]  # Ciudad3
]

calcular_promedio_temperaturas(temperaturas, ciudades, dias_semana, semanas)
