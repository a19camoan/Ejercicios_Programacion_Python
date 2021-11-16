'''
    Programa que pida cinco números enteros y diga cuál es el mayor.

    Autor: Andrés Castillero Moriana

    Fecha: 08/11/2021

    Algoritmo:
        Pedimos los 5 números enteros.
        Suponemos que el primer número (num1) es el mayor y lo almacenamos en otra variable.
        Comparamos el mayor actual con el siguiente número:
            si es mayor se compara con el siguiente.
            si no, el número comparado será el mayor actual.
        Se muestra el resultado en pantalla.

    Variables:
        num1: (int)
        num2: (int)
        num3: (int)
        num4: (int)
        num5: (int)
        maxi: (int)
'''
print("Progama que pide 5 números enteros y dice el mayor de ellos.")

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))
num4 = int(input("Introduzca el cuarto número: "))
num5 = int(input("Introduzca el quinto número: "))

# Inicializamos maxi con el primer número para empezar la comparación.
maxi = num1

if maxi < num2:
    maxi = num2
if maxi < num3:
    maxi = num3
if maxi < num4:
    maxi = num4
if maxi < num5:
    maxi = num5


''' 
Versión usando for:

    # i recorrerá cada número introducido.
    for i in [num1, num2, num3, num4, num5]:
        # Si maxi es menor que el número recorrido, maxi pasará a ser igual a ese número.
        if maxi < i:
            maxi = i
'''

print("Num max: ", maxi)
