'''
    Calcular la media de tres números pedidos por teclado.
    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo: 
        Se piden 3 números.
        Se calcula la media.

    Variables: 
        num1 (real): Introducido por el usuario. Usado para calcular la media.
        num2 (real): Introducido por el usuario. Usado para calcular la media.
        num3 (real): Introducido por el usuario. Usado para calcular la media.

'''

#Presentación del programa.
print("Programa que calcular la media de tres números.")

#Petición de datos.
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))
num3 = float(input("Introduzca el tercer número: "))

#Salida de datos.
print("La media es:", (num1+num2+num3) / 3)