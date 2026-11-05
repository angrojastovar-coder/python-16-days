'''
El Ejercicio: El Detector de Camisetas Temáticas

Imagina que eres el organizador de un evento y tienes varias cajas de ropa. Cada caja
contiene una lista de camisetas de diferentes colores.

Tu misión es encontrar cuáles cajas son "Temáticas de Navidad". 
La regla es muy clara: para que una caja sea considerada navideña, debe tener al menos
una camiseta de color "verde" Y al menos una camiseta de color "rojo". Si le falta 
alguno de los dos colores, no sirve.
    - Caja 1: ["azul", "verde", "blanco", "rojo"] ➔ ¡Navideña! (Tiene verde y tiene rojo).
    - Caja 2: ["rojo", "amarillo", "negro"] ➔ No sirve (Le falta el verde).
    - Caja 3: ["verde", "gris", "rosa"] ➔ No sirve (Le falta el rojo).
'''

def encontrar_caja_Navidad(cajas):
    caja_navidad = ["verde",  "rojo"]
    cajas_temáticas_navidad = []

    for caja in cajas:
        is_navideña = True
        for color in caja_navidad:
            if color not in caja:
                is_navideña = False
                break
        if is_navideña:
            cajas_temáticas_navidad.append(caja)
    return cajas_temáticas_navidad

cajas_navideñas = [["azul", "verde", "blanco", "rojo"], ["rojo", "amarillo", "negro", "verde"], ["verde", "gris", "rosa"]]
print(encontrar_caja_Navidad(cajas_navideñas))