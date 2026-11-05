'''
Repaso: Avanzado

3.1: ¿Es primo?
Crea es_primo(n). Un primo solo es divisible entre 1 y él mismo (el 1 no es primo).
'''

def es_primo(n):
    if n < 2:          # ¿qué números menores a este NO son primos?
        return False

    for i in range(2, n):      # ¿hasta dónde reviso? (el final de range no se incluye)
        if n % i == 0:
            return False
    return True

numero = 13

if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} No es primo")

def primos_hasta(n):
    lista = []
    for i in range(2, n+1):
        if es_primo(i):
            lista.append(i)
    return lista

resultado = primos_hasta(20)
print(resultado)
    