'''
Repaso: Avanzado

2.1: Promedio flexible
Crea promedio(*notas). Si no recibe notas, devuelve 0.
'''

def promedio(*notas):
    if len(notas) > 0:
        suma = sum(notas)
        return suma/len(notas)
    else:
        return 0    

resultado = promedio()
print(resultado)