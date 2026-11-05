'''
Repaso: Calentamiento

Ejercicio 3.2: Año bisiesto
Crea es_bisiesto(anio). Un año es bisiesto si:

es divisible entre 4, y
NO es divisible entre 100, salvo que sea divisible entre 400.
'''

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return f"Es un año bisiesto"
    return f"No es bisiesto"

resultado = es_bisiesto(2000)
print(resultado)
