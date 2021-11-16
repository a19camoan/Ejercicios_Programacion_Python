'''
    Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que
    tipo de triangulo es, teniendo en cuenta los siguiente:

        Si se cumple Pitágoras entonces es triángulo rectángulo.
        Si sólo dos lados del triángulo son iguales entonces es isósceles.
        Si los 3 lados son iguales entonces es equilátero.
        Si no se cumple ninguna de las condiciones anteriores, es escaleno.

    Autor: Andrés Castillero Moriana

    Fecha: 19/10/2021

    Algoritmo:
        Pedimos los datos necesarios.
        Con una estructura if-elif-else:
            1. Si se cumple Pitágoras entonces es triángulo rectángulo.
            2. Si sólo dos lados del triángulo son iguales entonces es isósceles.
            3. Si los 3 lados son iguales entonces es equilátero.
            4. Si no se cumple ninguna de las condiciones anteriores, es escaleno.

    Variables:
        sidea: (float) Introducido por el usuario. Uno de los lados.
        sideb: (float) Introducido por el usuario. Uno de los lados.
        sidec: (float) Introducido por el usuario. Uno de los lados.
'''

print("Programa que identifica los tipos de triángulos.")

# Petición de los lados.
sidea = float(input("Introduzca el valor del lado A: "))
sideb = float(input("Introduzca el valor del lado B: "))
sidec = float(input("Introduzca el valor del lado C: "))

# TODO print(max(sidea, sideb, sidec))

# Evaluación de condiciones con if-elif-else y salida del resultado.
if sidea**2 == sideb**2 + sidec**2:
    print("El triángulo es rectángulo.")
elif sidea == sideb and sidea == sidec and sideb == sidec:
    print("El triángulo es equilátero.")
elif sidea == sideb or sidea == sidec or sideb == sidec:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
