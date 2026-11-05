'''
Acumulador:

Crea una función que sume solo los números pares de una lista. 
'''
def sumar_numeros_pares(lista):
    suma = 0
    return (suma for l in lista if l % 2 == 0)

numeros = [1, 4, 7, 3, 5, 8, 9]
print(sumar_numeros_pares(numeros))
