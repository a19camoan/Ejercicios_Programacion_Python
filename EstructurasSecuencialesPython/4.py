'''
    Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirán ambos números.
        Se mostrará el resultado a la vez que se calcula el resultado mostrado.

    Variables:
        num1 (real): Introducido por el usuario. Será usado para realizar las operaciones pedidas.
        num2 (real): Introducido por el usuario. Será usado para realizar las operaciones pedidas.

'''

# Presentación del programa al usuario.
print("Programa que dados dos números, muestra la suma, resta, división y multiplicación de estos.")

# Petición de datos.
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

# Aplicación de las fórmulas y salida de datos.
print("La suma entre", num1, "y", num2, "da como resultado", round(num1+num2, 2))
print(f"La suma entre {num1} y {num2} da como resultado {num1+num2:.2}")

print("La resta entre", num1, "y", num2, "da como resultado", round(num1-num2, 2))
print("La división entre", num1, "y", num2, "da como resultado", round(num1/num2, 2))
print("La multiplicación entre", num1, "y", num2, "da como resultado", round(num1*num2, 2))