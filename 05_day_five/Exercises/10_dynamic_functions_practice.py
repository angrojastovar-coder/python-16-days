'''
Práctica Funciones Dinámicas 3:

Crea una función (cantidad_pares) que cuente la cantidad de números pares
que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
'''

lista_numeros =  [1, 2, 3, 6, 8, 9, 12, 15, 20]

def cantidad_pares(lista):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma = suma + 1
    return suma

resultado = cantidad_pares(lista_numeros)
print(resultado)

