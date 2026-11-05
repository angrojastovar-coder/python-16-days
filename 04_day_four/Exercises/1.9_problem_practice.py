'''
Nivel 3: Retos

3.2: Tarifa de envío
Crea costo_envio(peso, es_urgente):

peso hasta 1 kg → base de 5000
más de 1 hasta 5 kg → base de 8000
más de 5 kg → base de 12000
si es urgente, se suma 4000 a la base
'''

def  costo_envio(peso, es_urgente):
    if peso <= 1:
        costo = 5000
    elif peso <= 5:
        costo = 8000
    else:
        costo = 12000

    if es_urgente:
        costo += 4000
    return costo

print(costo_envio(10, True))
    