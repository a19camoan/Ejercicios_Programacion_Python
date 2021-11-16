'''
    Programa que dice si un número es par o impar

    Autor: Andrés Castillero Moriana
    Fecha: 19/10/2021

    Algoritmo:
        Se pedirá un número
        Con una estructura if-else se usará el operador módulo (%) entre 2
                1. Si el resultado es 0, el número es par.
                2. Si el resultado es 1,el número es impar.

    Variables a usar:
        num: (int) será introducido por el usuario para después ser comparado
'''

print("Programa que dice si un número es par o impar")

# Petición del número
num = int(input("Introduzca el número (entero): "))

# Comparación y salida del resultado
if num%2 == 0:
    print("El número", num, "es par.")
else:
    print("El número", num, "es impar.")
