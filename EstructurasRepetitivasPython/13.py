"""
    Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

    Autor: Andrés Castillero Moriana.

    Fecha: 09/11/2020

    Algoritmo:
        Se pide la cadena.
        Si la cadena es mayúscula:
            Se pasa la cadena a minúscula.
        Si no:
            Se pasa a mayúscula.


    Variables:
        string (str)
"""

string = input("Introduzca la cadena: ")

if string == string.upper():
    print(string.lower())
else:
    print(string.upper())
