'''
Crea una función llamada generar_factura que reciba el nombre_cliente 
y una lista de compras usando **kwargs (donde la llave es el producto y
el valor es el precio).La función debe armar un texto que liste los productos
y sus precios, uno al lado del otro."
'''

def generar_factura(nombre, **kwargs):
    mensaje = f"Querido/a {nombre}\n"

    for producto, precio in kwargs.items():
        mensaje += f"{producto} vale {precio}\n"
    return mensaje

print(generar_factura("Ana", pantalon=400, camisa=500))


def calcular_experiencia(puntos_base, bonus):
    total = puntos_base + bonus
    return total  # Muestra el resultado de inmediato

# Llamada actual:
print(calcular_experiencia(100, 50))
