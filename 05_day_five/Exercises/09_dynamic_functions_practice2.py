'''
Práctica Funciones Dinámicas 2:

Crea una función (suma_menores) que sume los números de una lista 
(almacenada en la variable lista_numeros) siempre y cuando sean mayores 
a 0 y menores a 1000, y devuelva el resultado de dicha suma.
'''

lista_numeros = [1, 4, 1, -6, 8]


def suma_menores(lista):
    sum = 0
    for l in lista:
        if l > 0 and l < 1000:
            sum = sum + l
    return sum

resultado = suma_menores(lista_numeros)
print(resultado)