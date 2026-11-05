'''
Repaso: Avanzado

2.3: Filtrar
Crea filtrar_mayores(lista, minimo) que devuelva una lista nueva solo con los números mayores que minimo.
'''

def filtrar_mayores(lista, minimo):

    nueva_lista = []

    for i in lista:
        if i > minimo:
            nueva_lista.append(i)
    return nueva_lista

resultado = filtrar_mayores([1, 8, 3, 10, 5], 4)
print(resultado)