'''
Repaso: Avanzado

3.3: Estadísticas
Crea estadisticas(*numeros) que devuelva tres valores: mínimo, máximo y promedio.
'''

def estadisticas(*numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, promedio = estadisticas(4, 9, 1, 6)
print(minimo, maximo, promedio)