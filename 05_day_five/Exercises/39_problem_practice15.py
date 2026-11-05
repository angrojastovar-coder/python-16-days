'''
Ejercicio: El Validador de Contraseñas Seguras

Tienes una lista de contraseñas creadas por usuarios. Quieres encontrar
cuáles son seguras. 
La regla es muy clara: para que una contraseña sea segura, debe contener 
obligatoriamente el carácter "$"_ Y el carácter "#"_.
    - "pass$word#" ➔ Segura (Tiene ambos).
    - "secret$123" ➔ Insegura (Le falta el #).
    - "admin1234" ➔ Insegura (Le faltan ambos).

Pista: Recuerda que un texto en Python se puede recorrer o revisar con in 
igual que una lista.
'''

def encontrar_contrasenas_seguras(lista):
    contrasenas_seguras = []

    for contraseña in lista:
        if "$" in contraseña and "#" in contraseña:
                contrasenas_seguras.append(contraseña)
    return contrasenas_seguras

print(encontrar_contrasenas_seguras(["pass$word#", "secret$123", "admin1234"]))