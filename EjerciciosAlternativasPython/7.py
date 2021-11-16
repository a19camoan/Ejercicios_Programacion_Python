'''
    Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
      * El exponente sea positivo, sólo tienes que imprimir la potencia.
      * El exponente sea 0, el resultado es 1.
      * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

    Autor: Andrés Castillero Moriana.
    Fecha: 19/10/2021

    Algoritmo:
        Se pedirá una letra
        Con una estructura if-elif-else:
            1.Si el exponente es 0, el resultado será 1.
            2.Si el exponente es mayor que 0, se realiza la potencia.
            3.Si el exponente es negativo el resultado es 1/potencia con el exponente positivo.

    Variables a usar:
        base: (float) Introducido por el usuario. Será elevado al exponente.
        exponent: (float) Introducido por el usuario. Indica el exponente de la base.
'''

print("Programa que calcula la potencia de un número.")

# Pedimos ambos números
base = float(input("Introduzca la base: "))
exponent = float(input("Introduzca el exponente: "))

# Estructura if-elif-else
if exponent == 0:
    print("El resultado es: 1")
elif exponent < 0:
    exponent *= -1
    print("El resultado es: 1/", base**exponent, sep="")
else:
    print("El resultado es:", base**exponent)
