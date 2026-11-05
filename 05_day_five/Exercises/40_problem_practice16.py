'''
Ejercicio: El Filtro de Agencias de Viajes (Destinos Soñados)

Tienes una lista de agencias de viajes. Cada agencia ofrece una lista de ciudades
destino. 

Un cliente quiere viajar y exige que la agencia ofrezca sí o sí vuelos a "París" 
Y a "Tokio". Encuentra qué agencias cumplen el requisito.
    - Agencia A: ["Madrid", "París", "Nueva York", "Tokio"] ➔ Aprobada.
    - Agencia B: ["Tokio", "Roma", "Londres"] ➔ Rechazada (Le falta París).
'''

def encontrar_agencias(diccionario_agencias):
    agencias_correctas = []

    for agencia, paises in diccionario_agencias.items():
        if "París" in paises and "Tokio" in paises:
            agencias_correctas.append(agencia)
    return f"Agencias aprobadas = {agencias_correctas}"

listado_agencias = {"Agencia A":["Madrid", "París", "Nueva York", "Tokio"], 
                    "Agencia B": ["Tokio", "Roma", "Londres"]}

print(encontrar_agencias(listado_agencias))
