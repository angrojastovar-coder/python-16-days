'''
El Escáner de Montañas (Picos Más Altos)

Crea una función que reciba una lista de alturas (números) y devuelva una nueva 
lista que solo contenga los números que son estrictamente mayores que TODOS los 
números que aparecieron antes que él.

El primer número de la lista siempre se incluye porque no tiene a nadie atrás.

Ejemplo: [3, 2, 5, 4, 8, 7]Explicación: El 3 entra (es el primero). El 2 no entra 
(es menor que 3). El 5 entra (es mayor que todos los anteriores: 3 y 2). El 4 no 
(es menor que 5). El 8 entra (es mayor que todos). El 7 no.Debe devolver: [3, 5, 8]
'''

def escaner_de_montañas(alturas):
    mayores = []
    anterior = alturas[0]

    for actual in alturas:
        if actual >= anterior:
            mayores.append(actual)
            anterior = actual
    return mayores

print(escaner_de_montañas([3, 6, 2, 4, 1]))