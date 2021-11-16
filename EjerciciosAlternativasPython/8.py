'''
    Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad
    es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen
    dichas condiciones se debe mostrar ‘NO ACEPTADA’.

    Autor: Andrés Castillero Moriana.

    Fecha: 19/10/2021

    Algoritmo:
        Con una estructura if-elif-else:
            1. Si la nota es mayor o igual a 5, la edad es mayor o igual a 18 y el sexo es F. ACEPTADA.
            2. Si todo lo anterior se cumple pero el sexo es M. POSIBLE.
            3. Si nada se cumple, NO ACEPTADA.

    Variables:
        nota: (float) Introducida por el usuario. Se usará para comprobar los requisitos.
        edad: (int) Introducida por el usuario. Se usará para comprobar los requisitos.
        sexo: (str) Introducida por el usuario. Se usará para comprobar los requisitos.
'''

print("Programa que escrbirá ACEPTADA, POSIBLE o NO ACEPTADA dependiendo de los requisitos")

# Petición de datos
nota = float(input("Introduzca su nota: "))
edad = int(input("Introduzca su edad: "))
sexo = input("Introduzca su sexo (M o F): ")

# Estructura
if nota >= 5 and edad >= 18 and sexo == "F" or sexo == "f":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo== "M" or sexo == "m":
    print("POSIBLE")
else:
    print("NO ACEPTADA")
