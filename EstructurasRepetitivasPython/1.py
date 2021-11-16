"""
    Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
    A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el
    introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina
    cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de
    intentos te muestra el número que había generado.

    Autor: Andrés Castillero Moriana.

    Fecha: 13/11/2021

    Algoritmo:
        -Se creará un número aleatorio (del 1 al 100) importando la función "random".
        -Se le pedirá al usuario un número.
        -Se comparará con el número  generado y se indicará si es mayor o menor que el número introducido.
        -El usuario tendrá 10 intentos.
        -El programa terminará si se ha llegado al límite de intentos o se ha adivinado el número.
        -Si se adivina, se mostrará también el número de intentos.

    Variables:
        num_aleatorio: (int) Número generado aleatoriamente.
        num_usuario: (int) Número introducido por el usuario.
        cont: (int) Contador utilizado para saber el número de intentos del usuario.
"""

# Importamos la biblioteca "random".
import random

# Generamos el número y le damos el valor 0 al contador.
num_aleatorio = int((random.randrange(100) + 1))
intentos = 0

print("¡Intenta adivinar el número!.")
print("Tendrás 10 intentos y el número es entero entre 1 y 100.")

# Pedimos el número al usuario.
num_usuario = int(input("Introduzca su número: "))

# Mientras los números sean distintos o el contador sea menor que 10 indicará si
#  es mayor o menor y pedirá otro número.
while num_usuario != num_aleatorio and intentos < 10:
    intentos += 1
    print("Te quedan", 10 - intentos, "intentos.")
    if num_usuario < num_aleatorio:
        num_usuario = int(input("El número es mayor. Inténtalo de nuevo: "))
    else:
        num_usuario = int(input("El número es menor. Inténtalo de nuevo: "))

# Si el contador es 10 o adivina el número, se le indica al usuario.
if intentos == 10:
    print("Has llegado al límite de intentos. El número es:", num_aleatorio)
else:
    print("¡Felicidades! Has necesitado", intentos, "intentos.")
