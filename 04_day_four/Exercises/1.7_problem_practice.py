'''
2.3: Triángulo
Crea tipo_triangulo(a, b, c) con los tres lados:

los tres iguales → "equilátero"
exactamente dos iguales → "isósceles"
todos distintos → "escaleno"
'''

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or b == c or a == c:
        return "isóceles"
    return "escaleno"

resultado = tipo_triangulo(3, 4, 5)
print(resultado)