'''
    Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones
    por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo: 
        Se pedirá el sueldo base y el valor de sus 3 ventas
        Se imprimirá por pantalla la comisión del 10% de las 3 ventas y la suma del sueldo base y la comision total.

    Variables:
        sueldo (real): Introducido por el usuario. Utilizado para calcular la comisión.
        venta1 (real): Introducido por el usuario. Utilizado para calcular la comisión.
        venta2 (real): Introducido por el usuario. Utilizado para calcular la comisión.
        venta3 (real): Introducido por el usuario. Utilizado para calcular la comisión.
        
'''

sueldo = float(input("Introduzca su sueldo base: "))
venta1 = float(input("Introduzca el valor de la primera venta: "))
venta2 = float(input("Introduzca el valor de la segunda venta: "))
venta3 = float(input("Introduzca el valor de la tercera venta: "))

#Se podría simplificar la salida de texto creando una tercera variable para calcular la comisión.
print("Cobrará", (venta1+venta2+venta3)*0.1, "€ por comsiones y en total", round(sueldo + (venta1+venta2+venta3)*0.1, 2), "€")