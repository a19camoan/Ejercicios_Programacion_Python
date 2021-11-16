"""
    Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
    el programa termina cuando se introduce un espacio.

    Autor: Andrés Castillero Moriana.

    Fecha: 03/11/2020

    Algoritmo:
        -Pedimos el carácter inicial para entrar en el bucle.
        -El bucle se repetirá hasta que el usuario pulse la tecla espacio.
        -Si la cadena introducida no es una vocal escribirá VOCAL.
        -Si no, escribirá NO VOCAL.
        -Al finalizar el bucle nos despedimos.

    Variables:
        caracter: (str) Introducida por el usuario.
"""
VOCALES = "AEIOUaeiou"

print("Programa que dice cual letra es una vocal tantas veces como el usuario quiera.")

# Pedimos el carácter inicial.
caracter = str(input("Introduzca un carácter: "))

# Si lo introducido no es de longitud 1 y alfabético, pediremos de nuevo el carácter.
while caracter.isalpha() != True or len(caracter) != 1:
    caracter = str(input("Introduzca un carácter: "))

# Bucle que escribe VOCAL si es una o NO VOCAL si no. Se detiene al pulsar el espacio.
while caracter != " ":
    if caracter in VOCALES:
        print("VOCAL")
        caracter = str(input("Introduzca otro carácter para continuar\nSi quiere terminar pulse la tecla espacio: "))
    else:
        print("NO VOCAL")
        caracter = str(input("Introduzca otro carácter para continuar\nSi quiere terminar pulse la tecla espacio: "))
