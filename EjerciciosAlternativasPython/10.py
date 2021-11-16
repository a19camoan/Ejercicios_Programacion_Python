'''
    Programa que indica la posición relativa de dos circunferencias

    Autor: Andrés Castillero Moriana

    Fecha: 19/10/2021

    Algoritmo:
        Pedimos los datos necesarios.
        Calculamos la distancia entre ambas circunferencias.
        Con una estructura if-elif-else:
            1. Si la distancia es 0, son interiores concéntricas.
            2. Si la distancia > suma de sus radios, son exteriores.
            3. Si la distancia = suma de sus radios, son tangentes exteriores.
            4. Si la distancia < suma de sus radios y > su diferencia, son secantes.
            5. Si la distancia = diferencia de sus radios, son tangentes interiores.
            6. Si todo lo demás no se cumple, son interiores.

    Variables:
        x1: (float) Coordenada X del punto central del primer círculo
        y1: (float) Coordenada Y del punto central del primer círculo
        radious1: (float)
        x2: (float) Coordenada X del punto central del segundo círculo
        y2: (float) Coordenada Y del punto central del segundo círculo
        radious2: (float)
        range: (float) Se calcula para poder comparalas.
'''

print("Programa que indica la posición relativa de dos circunferencias.")

# Petición de datos
x1=float(input("Introduca la coordenada X del punto central de la primera circunferencia: "))
y1=float(input("Introduca la coordenada Y del punto central del primera circunferencia: "))
radious1=float(input("Introduca el radio de la primera circunferencia: "))

x2=float(input("Introduca la coordenada X del punto central del segunda circunferencia: "))
y2=float(input("Introduca la coordenada Y del punto central del segunda circunferencia: "))
radious2=float(input("Introduca el radio de la segunda circunferencia: "))

# Calculamos la distancia entre los dos puntos
range=round(((x2-x1)**2+(y2-y1)**2)**(1/2),1)

# Estructura if-elif-else
if x1==x2 and y1==y2:
    print("Las circunferencias son interiores concéntricas.")
elif  radious1+radious2<range:
    print("Las circunferencias son exteriores.")
elif radious1+radious2==range:
    print("Las circunferencias son tangentes exteriores.")
elif radious1+radious2>range and range>radious1-radious2:
    print("Las circunferencias son secantes.")
elif range==radious1-radious2:
    print("Las circunferencias son tangentes interiores.")
else:
    print("Las circunferencias son interiores.")
