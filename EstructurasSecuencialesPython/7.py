'''
    Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo: 
        Se pedirá la cantidad de minutos a convertir.
        Se restará los minutos dividos entre 60 con la parte entera de esa misma división para tener solamente la parte decimal, 
         posteriormente se pasará a minutos.
        Se dividirá la los minutos introducidos entre 60 para hacer la conversión a horas pero solo nos quedaremos con la parte entera.

    Variables
        mins (real -> entero): Será inicialmente introducido por el usuario para despues pasarlo a horas.
        restomins (entero): Calculado por el programa para guardar los minutos restantes.
'''

print("Programa que recibe una cantidad de minutos y muestra por pantalla a cuantas horas y minutos corresponde.")

mins = float(input("Escriba los minutos a convertir: "))

restomins = int(mins%60)
mins = int(mins//60)

print("Equivale a", mins, "horas y", restomins, "minutos.")