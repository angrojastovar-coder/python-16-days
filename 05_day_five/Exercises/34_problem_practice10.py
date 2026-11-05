'''
El Validador de Calificaciones:

El problema:
Imagina que eres un profesor. Te dan una lista de notas de un alumno (del 1 al 10).
Queremos una función llamada evaluar_alumno *notas) que haga lo siguiente:
    - Calcula la nota final usando el promedio de todas las notas.
    - Redondea ese promedio a un solo decimal. 
    - Aplica las siguientes reglas:
        - Si el promedio redondeado está entre 9.0 y 10.0, regresa el texto: 
        "Excelente" y la nota más alta que sacó.
        - Si el promedio redondeado está entre 6.0 y 8.9, regresa el texto: 
        "Aprobado".
        - Si el promedio es menor a 6.0, regresa el texto: "Reprobado"
         y la nota más baja que sacó.
'''
def evaluar_alumno(*args):
    prom = sum (args) / len(args)
    redondeado = round(prom, 1)

    if 9.0 <= redondeado <= 10.0:
        return(f'"Excelente" tu nota más alta fue {max(args)}')
    elif 6.0 <= redondeado <= 8.9:
        return(f'"Aprobado"')
    else:
        return(f'"Reprobado" tu nota más baja fue {min(args)}')

print(evaluar_alumno(8, 9, 10, 7))