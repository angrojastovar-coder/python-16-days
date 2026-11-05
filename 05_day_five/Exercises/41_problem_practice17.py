'''
Ejercicio: Control de Calidad en la Fábrica de Dulces

Una fábrica analiza cajas de caramelos. Cada caja tiene una lista de sabores. 

Para que una caja pase el control de calidad, NO debe contener ningún sabor amargo. 
Los sabores prohibidos son: "limón_ácido" y "café_amargo". 

Devuelve solo las cajas aprobadas.
    - Caja 1: ["fresa", "menta", "uva"] ➔ Aprobada.
    - Caja 2: ["fresa", "limón_ácido", "manzana"] ➔ Rechazada.
'''

def validar_sabores(cajas):
    cajas_aprovadas = []

    for lista_sabores in cajas:
        if "limón_ácido" not in lista_sabores and "café_amargo" not in lista_sabores:
            cajas_aprovadas.append(lista_sabores)
    return cajas_aprovadas

print(validar_sabores([["fresa", "menta", "uva"], ["fresa", "limón_ácido", "manzana"]]))