'''
    Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
    Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.

    Autor: Andrés Castillero Moriana.

    Fecha: 19/10/2021

    Algoritmo:


    Variables:
        euro: (int) Cantidad de euros introducidos por el usuario
'''

print("Programa que desglosa el mínimo de billetes y monedas introdocidos.")

euro=int(input("Ingrese la cantidad exacta sin euros (sin céntimos): "))

if euro>=500:
    print(euro//500,"billete/s de 500€")
    euro%=500
if euro>=200:
    print(euro//200,"billete/s de 200€")
    euro%=200
if euro>=100:
    print(euro//100,"billete/s de 100€")
    euro%=100
if euro>=50:
    print(euro//50,"billete/s de 50€")
    euro%=50
if euro>=20:
    print(euro//20,"billete/s de 20€")
    euro%=20
if euro>=10:
    print(euro//10,"billete/s de 10€")
    euro%=10
if euro>=5:
    print(euro//5,"billete/s de 5€")
    euro%=5
if euro>=2:
    print(euro//2,"moneda/s de 2€")
    euro%=2
else:
    print(euro,"moneda/s de 1€")
