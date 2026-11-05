'''
Ejercicio 4: El Organizador de Torneos de Videojuegos

Tienes una lista de equipos inscritos. Cada equipo es una lista con los nombres
de sus integrantes. 

El torneo es en parejas, por lo que la regla estricta es: solo se aprueban los 
equipos que tengan exactamente 2 integrantes (len(equipo) == 2). 

Devuelve los equipos aceptados.
    - Equipo 1: ["Juan", "Pedro"] ➔ Aprobado.
    - Equipo 2: ["Ana"] ➔ Rechazada (Falta jugador).
    - Equipo 3: ["Luis", "Carlos", "Marta"] ➔ Rechazada (Muchos jugadores).
'''

def encontrar_equipos(listado_integrantes):
    equipos_aceptados = []

    for integrantes in listado_integrantes:
        if (len(integrantes)) == 2:
            equipos_aceptados.append(integrantes)
    return equipos_aceptados

print(encontrar_equipos([["Juan", "Pedro"], ["Ana"], ["Luis", "Carlos", "Marta"]]))