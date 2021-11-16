from math import sqrt
#Exportamos sqrt para poder calcular raíces cuadradas.

'''
    Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:


    Variables:
        x1 (real): Introducido por el usuario. La coordenada x del primer punto la cual usaremos para calcular la distancia.
        y1 (real): Introducido por el usuario. La coordenada y del primer punto la cual usaremos para calcular la distancia.
        x2 (real): Introducido por el usuario. La coordenada x del segundo punto la cual usaremos para calcular la distancia.
        y2 (real): Introducido por el usuario. La coordenada y del segundo punto la cual usaremos para calcular la distancia.
'''

x1=float(input("Introduzaca la coordenada x del primer punto: "))
y1=float(input("Introduzaca la coordenada y del primer punto: "))
x2=float(input("Introduzaca la coordenada x del segundo punto: "))
y2=float(input("Introduzaca la coordenada y del segundo punto: "))

#Esta variable es prescindible pero la usaré para simplificar el print.
dist = round(sqrt((x2-x1)**2 + (y2-y1)**2), 3)

print("La distancia entre los 2 puntos es de:", dist, "u")