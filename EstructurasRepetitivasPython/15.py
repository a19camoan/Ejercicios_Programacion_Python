"""
    Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee
     igual adelante que atrás.

    Autor: Andrés Castillero Moriana.

    Fecha: 09/11/2020

    Algoritmo:

    Variables:
        reverse: (str)
        string: (str)
"""

# Le damos el valor de cadena vacía a la variable.
reverse = ""

string = input("Introduce una palabra: ")

for i in string:
    reverse = i + reverse

if string == reverse:
    print("La palabra", string, "es un palíndromo.")
else:
    print("La palabra", string, "no es un palíndromo.")