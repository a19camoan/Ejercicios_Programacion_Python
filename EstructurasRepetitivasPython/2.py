"""
    Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
    El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

    Autor: Andrés Castillero Moriana.

    Fecha: 13/11/2021

    Algoritmo:
        -Se pondrán los contadores a 0.
        -Se le pedirá al usuario el número de veces que se repetirá el bucle.
        -Se irán pidiendo tantos números como veces se repita el bucle.
        -Al pedir el número se comparará con 0 y sumará 1 al bucle que corresponda.
        -Mostramos el resultado al usuario.

    Variables:
        repeticiones: (int) Introducido por el usuario. Número de veces que se repetirá el bucle.
        num: (float) Introducido por el usuario. Números a comparar con 0.
        ceros: (int) Contador utilizado para saber la cantidad de 0.
        positivos: (int) Contador utilizado para saber la cantidad de números mayores que 0.
        negativos: (int) Contador utilizado para saber la cantidad de números menores que 0.
"""

# Iniciamos con valor 0 los contadores.
ceros = 0
positivos = 0
negativos = 0

print("Programa que pide números y dice cuales son mayores, menores o iguales a 0.")

repeticiones = int(input("Introduzca cuántos números va a introducir: "))

# Se repite el bucle tantas veces como el usuario ha indicado y se comparan los números introducidos.
for n in range(repeticiones):
    num = float(input("Introduzca un número: "))
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
    else:
        ceros += 1

print("Has escrito", positivos, "números positivos.")
print("Has escrito", negativos, "números negativos.")
print("Has escrito", ceros, "veces 0.")
