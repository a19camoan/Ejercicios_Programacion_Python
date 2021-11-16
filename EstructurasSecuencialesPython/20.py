'''
    Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirá el número monedas al usuario.
        Se convertirá el valor de la moneda a céntimos multiplicandolo por el número de monedas.
        Se sumará para obtener el valor total.
        Se transformará el valor a €.

    Variables:
        e2 (entero): Introducido por el usuario. Tiene el valor de 200 cénts.
        e1 (entero): Introducido por el usuario. Tiene el valor de 100 cénts.
        c50 (entero): Introducido por el usuario.
        c20 (entero): Introducido por el usuario.
        c10 (entero): Introducido por el usuario.
        totalcent (entero): Calculado por el programa. 
'''

#Presentación del programa.
print("Programa que nos dice cuanto dinero tenemos dada la cantidad de monedas de 2€, 1€, 50 cént., 20 cént. y 10 cént.")

#Petición de datos.
e2 = int(input("Introduzca el número de monedas de 2€ que tiene: "))
e1 = int(input("Introduzca el número de monedas de 1€ que tiene: "))
c50 = int(input("Introduzca el número de monedas de 50 cént. que tiene: "))
c20 = int(input("Introduzca el número de monedas de 20 cént. que tiene: "))
c10 = int(input("Introduzca el número de monedas de 10 cént. que tiene: "))

#Paso de euros a céntimos y suma total de céntimos.
totalcent = e2*200 + e1*100 + c50*50 + c20*20 + c10*10

#Conversión a euros.
totalcent = float(totalcent/100)

#Salida de datos.
print("Tiene en total", totalcent, "€")