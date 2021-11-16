'''
    Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

    Autor: Andrés Castillero Moriana.
    Fecha: 19/10/2021

    Algoritmo:
        Se pedirán dos números.
        Con una estructura if-else:
                1. Si el segundo número es 0, no se realiza la división avisando al usuario.
                2. Si el segundo número no es 0, se efectúa la división y se muestra el resultado.

    Variables a usar:
        num1: (float) introducido por el usuario para ser el dividendo.
        num2: (float) introducido por el usuario para ser el divisor.
'''

print("Programa que divide dos números")

# Petición de los números.
num1 = float(input("Introduzca el dividendo: "))
num2 = float(input("Introduzca el divisor: "))

# Ejecución del "if" con los dos posibles resultados.
if num2 == 0:
    print("No ha sido posible efectuar la operación.")
else:
    print("El resultado de la división es", round(num1/num2, 3))
