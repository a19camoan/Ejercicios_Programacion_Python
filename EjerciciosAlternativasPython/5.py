'''
    Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
    Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

    Autor: Andrés Castillero Moriana.
    Fecha: 19/10/2021

    Algoritmo:
        Se pedirán ambas edades.
        Con una estructura if-else:
            La edad de la primera persona es menor que la de la segunda.
            La edad de la segunda persona es menor que la de la primera.
            En cualquier otro caso la edad es la misma.

    Variables.
        edad1: (int) Será la edad de la primera persona y se usará para comparar cuál de ambas edades es mayor.
        edad2: (int) Será la edad de la segunda persona y se usará para comparar cuál de ambas edades es mayor.
'''

print("Programa que lee la edad de 2 personas y dice quien es la más jóven o si tienen la misma edad.")

# Petición de ambas edades.
edad1 = int(input("Introduzca la edad de la primera persona: "))
edad2 = int(input("Introduzca la edad de la segunda persona: "))

# Comparación de edades.
if edad1 < edad2:
    print("La más joven es la primera persona.")
elif edad2 < edad1:
    print("La más joven es la segunda persona.")
else:
    print("Ambas tienen la misma edad.")
