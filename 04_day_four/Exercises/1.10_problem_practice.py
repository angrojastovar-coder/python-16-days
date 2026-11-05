'''
Nivel 3: Retos

3.3: Año bisiesto en una sola condición
Reescribe es_bisiesto(anio) de la Serie 1 usando una sola línea con and, or y not.
💡 Pista: divisible entre 4 y (no divisible entre 100 o divisible entre 400).
'''

def  es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0 ) or anio % 400 == 0

print(es_bisiesto(2100))
    