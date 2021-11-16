'''
    Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirá el valor de los grados Fahrenheit.
        Se le aplicará la fórmula al número dado.
            (°F − 32) × 5 / 9 = °C
        El resultado será mostrado redondeado a los 2 decimales por comodidad.

    Variables:
        fahr (real): Dado por el usuario. Se usará para aplicarle la fórmula previamente mencionada.
        cels (real): Calculada por el programa. Será el dato mostrado al usuario.
'''

#Presentación del programa al usuario.
print("Programa que transforma grados Fahrenheit a grados Celsius.")

#Petición de datos.
fahr=float(input("Introduzca los grados Fahrenheit: "))

#Aplicación de la fórmula.
cels = (fahr - 32) * 5/9

#Salida de datos
print("El resultado de la conversión es:", round(cels, 2),"°C")