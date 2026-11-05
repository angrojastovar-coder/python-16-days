'''
Memoria: 

Crea una función que reciba una lista de números y devuelva True
si encuentra cualquier número repetido dos veces seguidas (por ejemplo:
[1, 5, 5, 3] -> True). Es igual al del cero, pero con cualquier número.
'''

def identificar_repetido(lista):
    anterior = None

    for actual in lista:
        if actual == anterior:
            return True
        anterior = actual
    return False

numeros = [1, 5, 2, 3, 3] 
print(identificar_repetido(numeros))
