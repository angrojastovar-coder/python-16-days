'''
Repaso: Calentamiento

Ejercicio 3.3: Descuento
Crea precio_final(precio, descuento=0) donde descuento es un porcentaje.
'''

def precio_final(precio, descuento=0):

    calcular_descuento = (100 - descuento) / 100
    return (precio * calcular_descuento)

resultado = precio_final(100,20)
print(resultado)