'''
El Interruptor de Luces (Detectar Cambios):

Crea una función que cuente cuántas veces cambia la tendencia en una
lista de luces o interruptores representados por cadenas de texto 
("ON" y "OFF"). Debe contar cada vez que pasamos de "ON" a "OFF" o de
"OFF" a "ON".Ejemplo: ["ON", "ON", "OFF", "ON", "OFF", "OFF"]

Explicación: De la posición 1 a la 2 cambió (ON -> OFF, va 1). 
De la 2 a la 3 cambió (OFF -> ON, van 2). De la 3 a la 4 cambió (ON -> OFF, van 3).
De la 4 a la 5 no cambió.Debe devolver: 3
'''

def contar_cambio_luces(luces):
    contador = 0
    luz_anterior = None

    for cambio_luz_actual in luces:
        if luz_anterior is not None and cambio_luz_actual != luz_anterior:
            contador += 1
        luz_anterior = cambio_luz_actual
    return contador

luces = ["ON", "ON", "OFF", "ON", "OFF", "OFF"]
print(contar_cambio_luces(luces)) 

