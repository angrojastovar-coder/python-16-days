'''
Práctica sobre Argumentos Indefinidos (**kwargs) 1:

Crea una función llamada cantidad_atributos que cuente la cantidad
de parémetros que se entregan, y devuelva esa cantidad como resultado.
'''

def cantidad_atributos(**kwargs):
    return len(kwargs)

resultado = cantidad_atributos(x=5, y=2, b=2)
print(resultado)