"""
    Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

    Autor: Andrés Castillero Moriana.

    Fecha: 03/11/2020

    Algoritmo:
        Pedimos los 2 números al usuario.
        Recorremos el rango entre ambos número (incluido el último).
            Si es divisible entre 2, se imprimirá por pantalla.

    Variables:
        num1: (int)
        num2: (int)
"""

print("Programa que imprime todos los números pares entre dos números.")

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

# Intercambiamos valores en caso de que num1 sea mayor que num2.
if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2+1):
    if i%2 == 0:
        # Modificando el end del print hacemos que los números esten en una línea separados por un punto y un espacio.
        print(i, end=". ")
