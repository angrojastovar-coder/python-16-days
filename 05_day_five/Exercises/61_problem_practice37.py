'''
Repaso: Avanzado

2.4: Perfil
Crea crear_perfil(nombre, **extras) que devuelva un diccionario con nombre y todos los extras.
'''

def crear_perfil(nombre, **extras):
    perfil = {"nombre": nombre}
    perfil.update(extras)
    return perfil

resultado = crear_perfil("Gigi", ciudad="Florencia", rol="QA")
print(resultado)