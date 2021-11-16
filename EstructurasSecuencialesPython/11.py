'''
    Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo: 
        Se piden ambos números.
        Se restan y se calcula el valor absoluto para tener la distancia entre ambos números.

    Variables:
        num1 (real): Introducido por el usuario. Utilizado para calcular la distancia.
        num2 (real): Introducido por el usuario. Utilizado para calcular la distancia.
        
'''

print("Programa que calcula la distancia entre 2 números.")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print("La distancia entre ambos números es de", round(abs(num1-num2)))