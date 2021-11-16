'''
    Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

    Autor: Andrés Castillero Moriana.
    Fecha: 19/10/2021

    Algoritmo:
        Se pedirá una letra
        Con una estructura if-else:
            1. Se comprobará si es una letra, en caso de que sea así:
                1. Si la letra está comprendida entre las mayúsculas, dirá que es mayúscula.
                además, si la letra es "Ñ" dirá que es mayúscula.
                (Esto es así ya que la Ñ y ñ están separadas del resto de letras)
                2. Si no, es minúscula.
            2. En caso contrario se avisará al usuario de que no ha introsucido una letra.

    Variables a usar:
        letter: (str) introducido por el usuario.
'''

print("Programa que dice si es una letra es mayúscula o no.")

# Petición de la letra.
letter=input("Introduzca la letra: ")

# Comparación y salida de datos.
if len(letter)==1:
    if letter.isalpha() == True:
        if letter<="Z" and letter>="A" or letter<="Ú" and letter>="Á" or letter=="Ñ": # Se podría haber usado .isupper() para simplificar la línea.
            print("Es mayúscula.")
        else:
            print("No es mayúscula.")
    else:
        print("No ha introducido una letra.")
else:
    print("No es un carácter.")