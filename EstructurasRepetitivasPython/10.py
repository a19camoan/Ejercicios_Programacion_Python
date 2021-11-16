"""
    Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

    Autor: Andrés Castillero Moriana.

    Fecha: 09/11/2020

    Variables:
        string (str)
        character (str)
"""

char = 0

string = str(input("Introduce una cadena: "))
character = str(input("Introduce un carácter de la cadena: "))

# Nos aseguramos de que el carácter lo sea y este en la cadena.
while len(character) != 1 or character not in string:
    character = str(input("Introduce un carácter de la cadena: "))

# Recorremos toda la cadena.
for i in string:
    # Si encontramos una carácter que coincida con el introducido, se suma 1 al contador.
    if i == character:
        char += 1

print("Se repite", char, "veces.")
