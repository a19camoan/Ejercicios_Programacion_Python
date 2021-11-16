from math import sqrt
#Exportamos sqrt para poder calcular raíces cuadradas.

'''
    Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirán ambos catetos
        Se aplicará el teorema de Pitágoras.
            hipotenusa=√cateto1² * cateto2²
        Se mostrará el resultado redondeado a 2 decimales por comodidad.

    Variables:
        cat1 (real): Introducido por el usuario. Se le aplicará el teorema de Pitágoras.
        cat2 (real): Introducido por el usuario. Se le aplicará el teorema de Pitágoras.
'''

#Presentación del programa al usuario.
print("Programa que dados los catetos de un triángulo rectángulo, calcular su hipotenusa.")

#Petición de datos.
cat1 = float(input("Introduzca el valor del primer cateto: "))
cat2 = float(input("Introduzca el valor del segundo cateto: "))

#Aplicación de las fórmulas y salida de datos.
#Usamos la función sqrt().
print("La hipotenusa es:", round(sqrt(cat1**2 + cat2**2), 2))