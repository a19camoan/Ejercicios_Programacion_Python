'''
    Calcular el perí­metro y área de un rectángulo dada su base y su altura.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirá la base y altura del rectángulo.
        Se aplicarán las fórmulas para hayar el perímetro y el área.
            Las fórmulas son base*2 + altura*2 y base * altura respectivamente.
        Se mostrará en pantalla el resultado redondeado a 2 decimales por comodidad.

    Variables:
        base (real): Introducido por el usuario para calcular los datos requeridos.
        altura (real): Introducido por el usuario para calcular los datos requeridos.
'''

#Presentación del programa al usuario.
print("Programa que calcula el perí­metro y área de un rectángulo dada su base y altura.")

#Petición de datos
base = float(input("Introduzca la base: "))
altura = float(input("Introduzca la altura: "))

#Aplicación de las fórmulas y salida de datos.
print("El perímetro es:", round(base*2 + altura*2, 2), "u²")
print("El área es:", round(base * altura, 2), "u²")