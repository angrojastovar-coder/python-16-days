'''
Práctica sobre Argumentos Indefinidos (**kwargs) 2:

Crea una función llamada lista_atributos que devuelva en forma 
de lista los valores de los atributos entregados en forma de palabras
clave (keywords). La función debe preveer recibir cualquier cantidad de
 argumentos de este tipo."
'''

def lista_atributos(**kwargs):
    lista_convertida = []
    values = kwargs.values()

    for kwarg in values:
        lista_convertida.append(kwarg)
    return lista_convertida

print(lista_atributos(x=5, y=2, b=2, a="Ana"))