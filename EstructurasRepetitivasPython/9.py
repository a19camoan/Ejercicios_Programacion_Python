"""
    Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos
    mostrar.

    Autor: Andrés Castillero Moriana.

    Fecha: 13/11/2020

    Algoritmo:

    Variables:
        - (-)
"""

while True:
    repet = int(input("Introduzca la cantidad de números primos a mostrar. "))
    if repet > 0:
        break

# El primer primo es 2.
print("2")
