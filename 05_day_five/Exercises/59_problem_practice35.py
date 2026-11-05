'''
Repaso: Avanzado

2.2: Contar vocales
Crea contar_vocales(texto) (acumulador + for + if).
'''

def contar_vocales(texto):
    vocales = ["a","e","i","o","u"]
    encontradas = 0

    for letra in texto.lower():
        for vocal in vocales:
            if letra == vocal:
                encontradas += 1
    return encontradas

resultado = contar_vocales("Electroencefalografista")
print(resultado)