'''
Repaso: Calentamiento

Ejercicio 3.1: Una función que usa otra
Crea cuadrado(n) y luego suma_de_cuadrados(a, b) que use cuadrado.
'''

def cuadrado(n):
    return n * n

def suma_de_cuadrados(a,b):
    return a + b

resultado = suma_de_cuadrados(cuadrado(3),cuadrado(4))
print(resultado)
