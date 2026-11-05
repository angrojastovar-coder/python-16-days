'''
Nivel 2: Calentando motores

2.1: Entrada al cine
Crea precio_entrada(edad):

menores de 5 → 0
de 5 a 12 → 8000
de 13 a 59 → 15000
60 o más → 9000
'''

def precio_entrada(edad):
    if edad <= 5:
        return 0
    elif 5 <= edad <= 12:
        return 8000
    elif 13 <= edad <= 59:
        return 15000
    return 9000

resultado = precio_entrada(70)
print(resultado)