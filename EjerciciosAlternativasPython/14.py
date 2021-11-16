"""
    La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en
    tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño,
    se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente
    :
    si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2.
    Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un
    algoritmo para determinar la ganancia obtenida.

    Autor: Andrés Castillero Moriana

    Fecha: 19/10/2021

    Algoritmo:


    Variables:
        typ: (str)
        price: (float)
        size: (int)
        origin: (float)
"""

price = float(input("Introduzca el precio base del kilo de uva en céntimos: "))
typ = input("Introduzca el tipo de uva (A o B): ")
size = int(input("Introduzca el tamaño de uva (1 o 2): "))

# Guardamos el precio original para no machacarlo.
origin = price

# Modificamos el precio dependiendo del tipo y tamaño.
if typ == "A" or "a" and size == "1":
    price += 20
elif typ == "A" or "a" and size == "2":
    price += 30

if typ == "B" or "b" and size == "1":
    price -= 30
elif typ == "B" or "b" and size == "2":
    price -= 50

print("El precio final es", price, "cént./kg por lo que la ganancia es de", price-origin, "cént./kg.")
