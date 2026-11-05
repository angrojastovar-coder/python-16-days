'''
El Contador de Rachas (La Prueba de Fuego)

Crea una función que reciba una lista de lanzamientos de una moneda
(donde "C" es Cara y "X" es Cruz) y calcule cuál fue la racha más larga
de Caras seguidas ("C").Ejemplo: ["C", "X", "C", "C", "C", "X", "C", "C"]

Explicación: Primero hay 1 Cara. Luego hay una racha de 3 Caras seguidas. 
Al final hay una racha de 2 Caras seguidas. La racha máxima fue de 3.
Debe devolver: 3Pista: Vas a necesitar dos alcancías. Una para contar la racha
actual (que se reinicia a 0 si sale una "X") y otra para guardar el récord de
la racha más alta que hayas visto en todo el camino.
'''

def contar_rachas(lista_rachas):
    contador_racha_mayor = 0
    contador_racha_actual = 0

    for lista in lista_rachas:
        if lista == "C":
            contador_racha_actual += 1
            if contador_racha_actual > contador_racha_mayor:
                contador_racha_mayor = contador_racha_actual
        elif lista == "X":
            contador_racha_actual = 0    
    return contador_racha_mayor

print(contar_rachas(["C", "X", "C", "C", "C", "X", "C", "C"]))

