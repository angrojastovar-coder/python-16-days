'''
Práctica Funciones Dinámicas 1:

Crea una función (todos_positivos) que reciba una lista de números 
como parámetro, y devuelva True si todos los valores de una lista 
son positivos, y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
'''
nums_list = [1, 5, 5, -5, 5, 6, 100]

def todos_positivos(list):
    for l in list:
        if l <= 0:
            return False
    return True
resultado = todos_positivos(nums_list)

print(resultado)