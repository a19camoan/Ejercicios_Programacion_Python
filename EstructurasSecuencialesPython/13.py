'''
    Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna función predefinida que
    permita calcular la raíz cúbica, ¿cómo se puede calcular?

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirá el número al usuario.
        Se elevará a 1/3 el número.

    Variables:
        num (real): Introducido por el usuario. Se calculará su raíz cuadrada.
'''

print("Programa que calcula la raíz cúbica de un número.")

num = float(input("Introduzca el número: "))

print("La raíz cúbida de", num, "es", num**1/3)
