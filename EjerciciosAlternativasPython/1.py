"""
    Programa que dice si el primer número es mayor que el segundo

    Autor: Andrés Castillero Moriana
    Fecha: 19/10/2021

    Algoritmo:
        Serán pedidos ambos números
        Con una estructura if-elif-else podrán darse 3 posibles casos:
                1. EL primer número es mayor que el segundo
                2. El segundo número es mayor que el primero.

    Variables a usar:
        num1: (float) será introducido por el usuario para después ser comparado
        num2: (float) será introducido por el usuario para después ser comparado
"""

print("Programa que indica el mayor de dos número.")

# Petición de datos
num1 = input("Introduzca el primer número: ")
num2 = input("Introduzca el segundo número: ")

# Comparación y salida del resultado
if num1 < num2:
    print("El número ", num1, " no es mayor que ", num2)
elif num1 > num2:
    print("El número ", num1, " es mayor que ", num2)
else:
    print("Ambos números son el mismo.")
