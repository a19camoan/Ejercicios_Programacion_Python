"""
    Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el
    resultado de la potencia.
    No se puede utilizar el operador de potencia ni la función.

    Autor: Andrés Castillero Moriana.

    Fecha: 07/11/2020

    Algoritmo:

    Variables:
        base: (float)
        elevado: (float)
        exp: (int)
"""

base = float(input("Introduzca la base: "))
exp = int(input("Introduzca el exponente: "))

# Inicializamos la variable.
elevado = 1

# Cualquier número elevado a 0 es 1.
if exp == 0:
    print("El resultado es: 1")

for i in range(exp):
    pow *= base

print("El resultado es:", elevado)
print(base**exp)
