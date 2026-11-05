'''
Nivel 1: Calentamiento

1.1: Positivo o negativo
Crea signo(n) que devuelva "positivo", "negativo" o "cero".
'''

def signo(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

resultado = signo(0)
print(resultado)