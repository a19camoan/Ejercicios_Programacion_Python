"""
    Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el
    superior lo tiene que volver a pedir.

    A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las
    siguientes informaciones:

        La suma de los números que están dentro del intervalo (intervalo abierto).
        Cuantos números están fuera del intervalo.
        Informa si hemos introducido algún número igual a los límites del intervalo.

    Autor: Andrés Castillero Moriana.

    Fecha: 08/11/2020

    Variables:
        out (int)
        inside (0)
        equal (boolean)
        inf_limit (float)
        upp_limit (float)
"""

# Inicializamos
inside = 0
out = 0
equal = False

# Pedimos el intervalo
inf_limit = int(input("Introduce el límite inferior del intervalo: "))
upp_limit = int(input("Introduce el límite superior del intervalo: "))

while inf_limit < upp_limit:
    print("El límite inferior no puede ser mayor al superior,vuelve a introducir los limites.")
    inf_limit = int(input("Introduce el límite inferior del intervalo: "))
    upp_limit = int(input("Introduce el límite superior del intervalo: "))

# Pedimos el numero que se va a usar
num = int(input("Introduce un número: "))
while num != 0:
    if inf_limit < num < upp_limit:
        inside += num
    else:
        out += 1
        if num == inf_limit or num == upp_limit:
            equal = True
    num = int(input("Introduce un número (pulse 0 para salir): "))

# Resultados
print("La suma de los números dentro del intervalo es:", inside)
print("La cantidad de números fuera del intervalo es:", out)

if equal:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
