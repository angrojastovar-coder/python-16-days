'''
Repaso: Calentamiento

Ejercicio 2.3: Convertidor de temperatura
Crea celsius_a_fahrenheit(c). Fórmula: F = C × 9/5 + 32
'''

def celsius_a_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

resultado = celsius_a_fahrenheit(0)
print(resultado)
resultado = celsius_a_fahrenheit(100)
print(resultado)