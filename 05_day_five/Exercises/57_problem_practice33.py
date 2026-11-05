'''
Repaso: Avanzado

1.4: Contar datos
Crea contar_datos(**datos) que devuelva cuántos datos recibió.
'''

def contar_datos(**datos):
    contador = 0

    for clave, valor in datos.items():
        contador += 1
    return contador

resultado = contar_datos(nombre="Gigi", ciudad="Florencia")
print(resultado)