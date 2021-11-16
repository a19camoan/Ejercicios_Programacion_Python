'''
    Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirá el número de 2 cifras al usuario.
        Se imprimirá por pantalla la cadena con el orden invertido.

    Variables:
        cadena (cadena): Introducido por el usuario. Número pedido al usuario convertido en cadena.
'''

#Presentación del programa al usuario.
print("Programa que dado un número de dos cifras, da el número invertido.")

#Petición de datos.
cadena = str(input("Introduzca un número de 2 cifras: "))

#Salida de datos con la cadena invertida.
print("El número invertido es", cadena[1]+cadena[0])