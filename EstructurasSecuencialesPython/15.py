'''
    Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirá ambos números al usuario.
        La variable "a" será movida a la varible "c", la "b" a la "a" y por último la "c" a la "b".

    Variables:
        a (real): Introducido por el usuario.
        b (real): Introducido por el usuario.
        c (real): Introducido por el usuario.
'''

print("Programa que intercambia valores entre variables.")

a = input("Introduzca el primer número: ")
b = input("Introduzca el segundo número: ")

c = a
a = b
b = c

print("Ahora el primer número es", a, "y el segundo", b)