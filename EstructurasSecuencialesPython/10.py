'''
    Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
    * 55% del promedio de sus tres calificaciones parciales.
    * 30% de la calificación del examen final.
    * 15% de la calificación de un trabajo final.

    Autor: Andrés Castillero Moriana.
    Fecha: 09/10/2021

    Algoritmo: 
        Se piden las notas.
        Se calcula la nota final aplicando los porcentajes correspondientes.

    Variables:
        calificacion(entero): Introducido por el usuario. Se irá sumando conforme el usuario va introduciendo las notas para luego hacer la media.
        calificacion_final(entero): Introducido por el usuario. Se usará para calcular la nota final despues de aplicarle el 30%.
        trabajo (entero): Introducido por el usuario. Se usará para calcular la nota final despues de aplicarle el 15%.
        nota (real): Nota final
        
'''

calificacion = float(input("Introduzca la nota de su primera calificación: "))
calificacion += float(input("Introduzca la nota de su segunda calificación: "))
calificacion += float(input("Introduzca la nota de su tercera calificación: "))
calificacion_final = float(input("Introduzca la nota de su calificación final: "))
trabajo = float(input("Introduzca la nota de su trabajo final: "))

# Esta variable es prescindible pero la usaré para simplificar el print.
nota = round(((calificacion)/3)*0.55 + calificacion_final*0.3 + trabajo*0.15, 2)

print("Su nota final es:", nota)
