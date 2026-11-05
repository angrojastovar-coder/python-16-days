'''
Mixto: 

Crea una función que cuente cuántas veces un número es estrictamente
mayor que el número anterior (por ejemplo: en [1, 5, 3, 6], el 5 es mayor
que 1, y el 6 es mayor que 3. Debería devolver 2).
'''

def contar_veces_mayor(lista):
    lista_mayor = []
    mayor = lista[0]

    for actual in lista:
        if actual > mayor:
            lista_mayor.append(actual)
        mayor = actual
    return len(lista_mayor)

lista = [1, 5, 3, 6]
print(contar_veces_mayor(lista))