"""
    Realiza un programa en Python que pida una fecha en formato dd/mm/aaaa del siglo
    XXI, compruebe si es correcta, en caso de no serlo, señale el error correspondiente (en el
    dispositivo de errores) y acabe el programa de forma anormal, en caso de ser correcta, que muestre
    el día siguiente a la misma en el mismo formato.

    Autor: Andrés Castillero Moriana

    Fecha: 25/11/2021

    Algoritmo:

"""
import sys

print("Programa que muestra la siguiente fecha a la introducida.")

fecha_usuario = input("Introduzca la fecha en formato dd/mm/aaaa: ")

# Primero comprobamos la longitud de la cadena.
if len(fecha_usuario) != 10:
    print("Formato no válido.", file=sys.stderr)
    exit(1)

# Ahora comprobamos que contenga / donde debe estar.
if fecha_usuario[2] != "/" and fecha_usuario[5] != "/":
    print("Formato no válido.", file=sys.stderr)
    exit(1)

# Comprobamos si contiene caracteres.
for c in fecha_usuario:
    if c.isalpha():
        print("Hay caracteres en la fecha.", file=sys.stderr)
        exit(1)

# Partimos la fecha en día, mes y año.
dia = int(fecha_usuario[0] + fecha_usuario[1])
mes = int(fecha_usuario[3] + fecha_usuario[4])
ano = int(fecha_usuario[6] + fecha_usuario[7] + fecha_usuario[8] + fecha_usuario[9])

# Se comprueban ahora los años, los meses y los días.
if not (2000 <= ano <= 2099):
    print("Año no válido", file=sys.stderr)
    exit(1)

if not (1 <= mes <= 12):
    print("Mes no válido", file=sys.stderr)
    exit(1)

if not (1 <= dia <= 31):
    print("Día no válido", file=sys.stderr)
    exit(1)

# Caso concreto de enero
if mes == 2:
    if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
        if not (1 <= dia <= 29):
            print("Día no válido, debería ser 29 el día máximo", file=sys.stderr)
            exit(1)
    else:
        if not (1 <= dia <= 28):
            print("Día no válido, debería ser 28 el día máximo", file=sys.stderr)
            exit(1)

# Caso de meses con 30 y 31 días.
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if not (1 <= dia <= 30):
        print("Día no válido, debería ser 30 el día máximo", file=sys.stderr)
        exit(1)

# Sumamos 1 al día.
dia += 1

if mes == 2:
    if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
        if dia > 29:
            dia = 1
            mes = 3
    else:
        if dia > 28:
            dia = 1
            mes = 3
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        dia = 1
        mes += 1
else:
    if dia > 31:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1

# No sé cómo poner el formato correcto.
print(f"El día siguiente es: {dia}/{mes}/{ano}")
