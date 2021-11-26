"""
    Haz un programa que juegue al piedra/papel/tijera contra el ordenador, que usará números aleatorios para realizar
    la tirada. Después de cada jugada pregunta al usuario si quiere continuar, en caso negativo se muestra el número de
    partidas jugadas, las ganadas por cada jugador y las empatadas.

    Autor: Andrés Castillero Moriana

    Fecha: 25/11/2021

    Algoritmo:
        Se pide el número al usuario para saber su jugada.
        Se comprueba si es correcto lo introducido.
        En un bucle:
            Se compara el número del usuario con el aleatorio, pudiendo ganar la máquina, empatar o perder.
            Si el usuario introduce "n", se saldrá del bucle.
        Se muestran las estadísticas de las partidas por pantalla.
"""
import random

PIEDRA = 1
PAPEL = 2
TIJERA = 3

# Variables que se usarán como contadores para las estadísticas.
victorias = 0
derrotas = 0
empates = 0

# Se inicializa como espacio para entrar en el bucle.
confirmacion = " "

print("Programa para jugar a piedra, papel y tijera.")

while confirmacion.upper() != "N":
    mano_usuario = int(input("Introduzca piedra(1), papel(2) o tijera(3): "))

    # Comprobamos que el dato introducido por el usuario es válido.
    if mano_usuario < 1 or mano_usuario > 3:
        while True:
            mano_usuario = int(
                input("valor introducido no válido, por favor introduzca 1 para piedra, 2 para papel o 3 "
                      "para tijera: "))
            if 1 <= mano_usuario <= 3:
                break

    mano_maquina = random.randint(1, 3)

    if mano_maquina == mano_usuario:
        empates += 1
        print(f"¡Has empatado! La máquina ha sacado {mano_maquina}")
    elif mano_maquina == PIEDRA and mano_usuario == PAPEL or mano_maquina == TIJERA and mano_usuario == PIEDRA \
            or mano_maquina == PAPEL and mano_usuario == TIJERA:
        victorias += 1
        print(f"¡Has ganado! La máquina ha sacado {mano_maquina}")
    else:
        derrotas += 1
        print(f"¡Has perdido! La máquina ha sacado {mano_maquina}")

    confirmacion = input("¿Desea continuar (s/n)?: ")
    while confirmacion.upper() != "S" and confirmacion.upper() != "N":
        confirmacion = input("Por favor, introduzca \"s\" para continuar o \"n\" para terminar: ")

print(f"De {victorias + derrotas + empates} partidas jugadas:\nHas ganado {victorias} veces\nPerdido {derrotas} veces"
      f"Empatado {empates} veces.")
