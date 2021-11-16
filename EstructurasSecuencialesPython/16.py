'''
    Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor.
    Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar
    y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirán las 2 velocidades en km/h y la distancia en km.
        Se dividirá la distancia entre el resultado de la resta de ambas velocidades (v2-v1).
        Se multiplicará por 60 para pasar el tiempo de horas a minutos.

    Variables:
        vel1 (real): 
        vel2 (real): 
        dist (real): 
'''

print("Programa que calcula el tiempo requerido para un adelantamiento dadas ambas velocidades y la distancia entre ambos vehículos.")

vel1 = float(input("Introduzca la primera velocidad en km/h (la menor): "))
vel2 = float(input("Introduzca la segunda velocidad en km/h (la mayor): "))
dist = float(input("Introduzaca en kms la distancia: "))

tiempo = round((dist / (vel2 - vel1))*60, 2)

print("Tardará",tiempo,"minutos.")