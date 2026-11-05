'''
Repaso: Avanzado

1.2: Contar negativos
Crea contar_negativos(lista).
'''

def contar_negativos(lista):
    contar = 0

    for l in lista:
        if l < 0:
            contar += 1
    return contar

resultado = contar_negativos([3, -1, -5, 8, -2])
print(resultado)