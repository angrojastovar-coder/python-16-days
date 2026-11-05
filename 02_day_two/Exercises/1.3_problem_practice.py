'''
Nivel 2: Calentando motores

2.3: Minutos a horas
Pide un número de minutos y muestra cuántas horas completas y cuántos minutos sobran.
'''

minutos = int(input("Ingrese unos minutos: "))
horas = minutos // 60
minutos_sobrantes = minutos % 60

print(f"{minutos} minutos equivale a {horas} hora(s) y {minutos_sobrantes} minutos")