'''
Repaso: Calentamiento

Ejercicio 1.4: ¿Es par?
Crea es_par(n) que devuelva True si es par y False si no.
💡 Pista: el operador % te da el residuo de una división.
'''

def es_par(n):
    return n % 2 == 0

resultado = es_par(7)
print(resultado)