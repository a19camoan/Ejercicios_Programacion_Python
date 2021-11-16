"""
    · La política de cobro de una compañía telefónica es: cuando se realiza una llamada,
    el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos
    cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos,
    y a partir del décimo minuto, 50 céntimos.
    · Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y
    en turno de tarde, 10 %.
    · Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

    Autor: Andrés Castillero Moriana.
    Fecha: 22/10/2021

    Algoritmo:
        Se pregunta el tiempo en minutos de la llamada.
        Determinamos el impuesto a aplicar preguntando si es domingo:
            si la respuesta es "N", se pregunta si es el turno de tardes:
                si se responde "N" se le da el valor 1.15 a IMPUESTO
                si no, se le da el valor 1.1 a IMPUESTO
            si no, se le da el valor 1.03 a IMPUESTO


    Variables.
        tiempo: (int) Introducida por el usuario. Se usa para calcular el precio final y los distintos precios.
        domingo: (str) Introducido por el usuario. Se usa para determinar qué impuesto aplicar.
        tarde: (str) Introducido por el usuario. Se usa para determinar qué impuesto aplicar.
        IMPUESTO: (float) Se determina según los valores de "domingo" y "tarde" teniendo 3 valores posibles.
"""

print("Programa que calcula el precio de una llamada.")

tiempo = int(input("Escriba cuántos minutos ha durado la llamada: "))

# Comprobamos el impuesto a añadir.
domingo = input("¿Es domingo?(S/N) ")
if domingo.upper() == "N":
    tarde = input("¿Es turno de tardes?(S/N) ")
    if tarde.upper() == "N":
        # Impuestos de mañanas.
        impuesto = 0.15
    else:
        # Impuestos de tardes.
        impuesto = 0.1
else:
    # Impuestos de domingos.
    impuesto = 0.03

# Calculamos el coste de la llamada.
if tiempo <= 5:
    precio = tiempo * 100
elif tiempo <= 8:
    precio = 500 + (tiempo-5) * 80
elif tiempo <= 10:
    precio = 740 + (tiempo-8) * 70
else:
    precio = 880 + (tiempo-10) * 50

print(f"El precio final de la llamada es {precio * (1 + impuesto) / 100:.2f} €")
