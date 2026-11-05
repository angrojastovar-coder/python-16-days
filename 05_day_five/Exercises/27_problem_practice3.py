'''
Ejercicio 3:

Escribe una función que requiera una cantidad indefinida de argumentos.
Lo que hará esta función es devolver True si en algún momento se ha ingresado
al numero cero repetido dos veces consecutivas.

Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> Fals
'''
def numero_repetido(*args):
    anterior = None

    for actual in args:
        if actual == 0 and anterior == 0:
            return True
        anterior = actual
    return False

print(numero_repetido(5,6,1,0,0,9,3,5))
