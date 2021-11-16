"""
    Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y
     así sucesivamente.
    Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después de los 20
     meses.

    Autor: Andrés Castillero Moriana.

    Fecha: 07/11/2020

    Algoritmo:

    Variables:
        prize: (float)
        month: (int)
        total: (float)
"""

# Inicializamos las variables.
prize = 10
month = 1
total = 0  

for _ in range(20):
    print("En el mes", month, "tendrás que pagar: ", prize, "€")
    prize *= 2
    month += 1
    total += prize

print("El total a pagar es de:", total, "€")
