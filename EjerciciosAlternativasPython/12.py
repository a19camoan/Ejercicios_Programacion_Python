'''
    Escribir un programa que lea un año indicar si es bisiesto.

    Autor: Andrés Castillero Moriana.

    Fecha: 19/10/2021

    Algoritmo:
        Con una estructura if-else:
            1. Si se cumple que sea divisible por 4 o 400 pero no entre 100, es bisiesto.
            2. Si no lo cumple, no lo es.

    Variables:
        year: (int) Introducido por el usuario. Año a analizar.
'''

print("Programa que identifica los años bisiestos.")

# Petición del año.
year=int(input("Introduzca el año: "))

if year%100!=0 or year%400==0 and year%4==0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
