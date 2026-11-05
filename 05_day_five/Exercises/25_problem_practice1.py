'''
Ejercicio 1:

Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros. 

Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.

Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.

Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el
número de valor intermedio"
'''

def devolver_distintos(a, b, c):
    suma = a + b + c
    numeros = [a, b, c]

    if suma > 15:
        return max(devolver_distintos)
    elif suma < 10:
        return min(devolver_distintos)
    else:
        numeros.sort()
        return numeros[1]

print(devolver_distintos(7, 2, 4)) 