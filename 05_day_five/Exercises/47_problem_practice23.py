'''
Repaso: Calentamiento

Ejercicio 2.1: Mayor de dos
Crea mayor(a, b) que devuelva el número más grande. No uses max().
'''

def mayor(a,b):
    if a > b:
        return a
    return b

resultado = mayor(3,9)
print(resultado)