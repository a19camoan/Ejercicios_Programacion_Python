'''
    Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
    
    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Pedimos el nombre, apellido 1 y apellido 2.
        Mostramos las iniciales usando el índice de las cadenas.

    Variables:
        nombre (cadena): 
        apellido1 (cadena): 
        apellido2 (cadena): 
'''

nombre = input("Introduzca su nombre: ")
apellido1 = input("Introduzca su primer apellido: ")
apellido2 = input("Introduzca su segundo apellido: ")

print("Sus iniciales (por si no las sabías a estas alturas) son", nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper())