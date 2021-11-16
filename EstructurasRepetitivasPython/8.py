"""
    Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

    Autor: Andrés Castillero Moriana.

    Fecha: 07/11/2020

    Algoritmo:

    Variables:
        hour: (int)
        m: (int)
        s: (int)
"""

import time

print("Cronómetro de 24 horas.")

# Ciclo y Salida
for hour in range(0, 24):
    for minute in range(0, 60):
        for second in range(0, 60):
            print("H:", hour, "M:", minute, "S:", second, end="")
            print(8 * "\b", end="")
            time.sleep(1)
