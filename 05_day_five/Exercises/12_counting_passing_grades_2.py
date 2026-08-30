'''
Ejercicio 2: El contador de aprobados

- Objetivo: Crear una función llamada contar_aprobados(calificaciones) que 
reciba una lista de notas (de 0 a 100) y cuente cuántos alumnos aprobaron. 
Un alumno aprueba si su nota es mayor o igual a 60.
- Pista: En lugar de sumar las notas, crea una variable contador = 0 y súmale
 1 cada vez que encuentres una nota aprobatoria.
- Lista de prueba: [55, 90, 45, 78, 60, 100] (Debe dar como resultado 4).
'''

list_notes = [55, 90, 45, 78, 60, 100]

def contar_aprobados(calificaciones):
    suma = 0
    for i in calificaciones:
        if i >= 60:
            suma = suma + 1
    return suma

resultado = contar_aprobados(list_notes)
print(resultado)