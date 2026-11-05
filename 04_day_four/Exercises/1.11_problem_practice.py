'''
Nivel 3: Retos

3.4: Piedra, papel o tijera ✂️
Crea ganador(j1, j2) con jugadas "piedra", "papel" o "tijera". Devuelve "Empate", "Jugador 1" o "Jugador 2".
'''

def ganador(j1, j2):
    if j1 == j2:
        return "Empate"
    elif (j1 == "piedra" and j2 == "papel") or (j1 == "papel" and j2 == "tijera") or (j1 == "tijera" and j2 == "piedra"):
        return "Jugador 2"
    return "Jugador 1"

print(ganador("tijera", "tijera"))
    