'''
    Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo si el carácter leído
    es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada), «Es un dígito» si es un dígito,
    «Es otro carácter» si no es ninguno de los anteriores y «No es un carácter» si el usuario ha introducido más de un carácter.

    Autor: Andrés Castillero Moriana

    Fecha: 19/10/2021

    Algoritmo:
        Pedimos los datos.
        Primero se comprueba que se ha introducido un carácter, si es así:
            Usando el método isalpha comprobamos si es alfabético.
            Sino, comprobamos si es numérico con isnumeric
            Sino, los comparamos con los signos de puntuación.
            En otro caso, es otro carácter.
        En caso contrario no es un carácter.

    Variables:
        letra: (str) 
'''

print("Programa que dice si el carácter introduciso es un signo de puntuación, una letra, dígito u otro.")

letra = input("Introduzca el carácter: ")

if len(letra) == 1:
    if letra.isalpha == True:
        print("Es una letra.")
    elif letra.isnumeric == True:
        print("Es un dígito.")
    elif letra in ".,-+:;?¿!¡'\"[{()}]<=>%*@":
        print("Es signo de puntuación.")
    else:
        print("Es otro carácter.")
else:
    print("No es un carácter.")