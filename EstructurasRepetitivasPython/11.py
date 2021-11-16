"""
    Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
    realiza un programa que cuente cuantas palabras tiene.

    Autor: Andrés Castillero Moriana.
    Fecha: 15/11/2021

    Algoritmo:
        Se pide la frase.
        Se recorre "frase" para contar los espacios.
            si se detecta un espacio un contador suma 1
        El número de palabras será el número de espacios más 1 ya que cada palabra se separa por un espacio y las frases
         no acaban en espacio.

    Variables.
        espacios: (int)
        frase: (str)
"""

print("Programa que cuenta palabras.")
frase = input("Introduzca la frase: ")

espacios = 0

for i in frase:
    if i == " ":
        espacios += 1

print(f"Hay {espacios + 1} palabras.")

"""
Versión con el método .split(): 
Divide una cadena en una lista donde cada palabra es un elemento de una lista

frase_separada = frase.split()
numero_palabras = len(frase_separada)

print(f"Hay {numero_palabras} palabras.")
"""