'''
Ejercicio 11: El filtro de pares

- Objetivo: Crear una función que sume solo los números pares de una lista.
- Pista: Un número es par si al dividirlo entre 2 el residuo es cero. En Python
esto se evalúa con el operador de módulo: if l % 2 == 0:.
- Lista de prueba: [2, 3, 4, 7, 8] (Debe dar como resultado 14).
'''
list_numbers = [2, 3, 4, 7, 8]

def sum_pares(lista):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma = suma + i
    return suma

resultado = sum_pares(list_numbers)
print(resultado)