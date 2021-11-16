'''
    Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada respuesta correcta 5 puntos,
    por una incorrecta -1
    y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo:
        Se pedirá el número de preguntas correctas e incorrectas al usuario.
        El número respuestas correctas se multiplicará por 5 y las incorrectas por nada.
        Se restará el resultado y se imprimirá por pantalla.

    Variables:
        correcta (entero): Introducido por el usuario. Se multiplicará por 5.
        incorrecta (entero): Introducido por el usuario. Se le restará al valor de "correcta".
'''

print("Programa que calculará tu nota del examen.")

correcta = int(input("Introduzca el número de preguntas correctas: "))
incorrecta = int(input("Introduzca el número de preguntas incorrectas: "))
print("No se te pedirá el número de respuestas en blanco porque no influyen en la nota.")

print("Tu nota final es", correcta*5 - incorrecta)