'''
    Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo: 
        Se pide el precio de la compra.
        Se multiplica por 0.85 para restarle el 15% del valor.

    Variables:
        precio (real): Introducido por el usuario. Utilizado para calcular el precio final.
        
'''

precio = float(input("Introduzca el valor de su compra: "))

print("El precio final es de :", precio*0.85, "€")