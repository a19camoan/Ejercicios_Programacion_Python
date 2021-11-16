'''
    El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar
    a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros;
    de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros,
    sin importar el número de alumnos. Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno
    por el viaje.

    Autor: Andrés Castillero Moriana

    Fecha: 19/10/2021

    Algoritmo:
        Pedimos el número de alumnos.
        Si hay 100 o más alumnos, el precio será el número de estos por 65.
        Si no, se comprueba si es mayor o igual a 50 para multiplicar por 70 el número de alumnos.
        Si no, se comprueba si es mayor o igual a 30 para multiplicar por 95 el número de alumnos.
        Si no, el precio será de 4000€.

    Variables:
        prize: (float)
        studnt: (int)
'''

print("Programa que calcula el precio del viaje y el precio individual de cada alumno.")

studnt = int(input("Introduzca el número de alumnos que harán el viaje: "))

if studnt >= 100:
    prize = studnt*65
elif studnt >= 50:
    prize = studnt*70
elif studnt >= 30:
    prize = studnt*95
else:
    prize = 4000

print("El precio total es de", prize, "€ y el precio por alumno", prize/studnt, "€.")