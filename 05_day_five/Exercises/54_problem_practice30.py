'''
Repaso: Avanzado

1.1: Multiplicar todos
Crea multiplicar_todos(*numeros) que devuelva el producto de todos. Sin argumentos debe devolver 1.
'''

def multiplicar_todos(*numeros):
    multiplicado = 1

    for i in numeros:
        multiplicado *= i
    return multiplicado

resultado = multiplicar_todos()
print(resultado)