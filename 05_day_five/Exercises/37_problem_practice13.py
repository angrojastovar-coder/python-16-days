'''
Ejercicio: El Filtro de Compras Saludables

Imagina que eres un nutricionista y tienes una lista con los carritos
de compras de varios pacientes. Cada carrito es una lista de los productos
que compraron.
Quieres encontrar cuáles carritos son 100% saludables.

La regla de oro es que un carrito saludable no debe contener ningún producto
prohibido (los productos prohibidos son: "azúcar", "papas" y "gaseosa").

    - Si el carrito es ["manzana", "pollo", "arroz"], ¿tiene algún prohibido? No. 
¡Pasa la prueba! 
    - Si el carrito es ["manzana", "gaseosa", "lechuga"], 
¿tiene algún prohibido? Sí, la gaseosa. Se descarta de inmediato.
'''

def encontrar_carritos_saludables(carrito):

    productos_prohibidos = ["azúcar", "papas", "gaseosa"]

    for producto_actual in carrito:

        is_saludable = True

        for producto_prohibido in productos_prohibidos:
            if producto_prohibido in producto_actual:
                is_saludable = False
                return(f"No es saludable")

        if is_saludable:
            return f"Es un carrito saludable"

print(encontrar_carritos_saludables(["manzana", "pollo", "azúcar"]))