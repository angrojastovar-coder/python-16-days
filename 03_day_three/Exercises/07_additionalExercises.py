"""/ casos_de_prueba = []

casos_de_prueba.append("Login")
casos_de_prueba.append("Logout")
casos_de_prueba.append("Registro")
casos_de_prueba.append("Cuarto")
casos_de_prueba.append("Quinto")

casos_de_prueba.remove("Logout")

print(f"Estos son los casos de prueba que quedaron {casos_de_prueba}")
print(f"Este es el numero de casos de prueba que quedaron {len(casos_de_prueba)}")"""

"""dic_caso_de_prueba = {"nombre":"Ana", "estado":"pendiente", "prioridad":"Alta"}
print(f"Nombre: {dic_caso_de_prueba["nombre"]}")
print(f"Estado: {dic_caso_de_prueba["estado"]}")
print(f"Prioridad: {dic_caso_de_prueba["prioridad"]}")

dic_caso_de_prueba["estado"] = "Aprobado"
print(f"Nombre: {dic_caso_de_prueba["nombre"]}")
print(f"Estado: {dic_caso_de_prueba["estado"]}")
print(f"Prioridad: {dic_caso_de_prueba["prioridad"]}")"""

"""casos_de_prueba = {"nombre": "Ana", "estado": "Aprobado", "color": "Azul"}
for key in casos_de_prueba:
    print(key)"""

"""casos_de_prueba = [{"nombre": "Ana", "estado": "Aprobado", "color": "Azul"},
                   {"nombre": "Angela", "estado": "Reprobado", "color": "Rojo"},
                   {"nombre": "Rosa", "estado": "Eliminado", "color": "negro"}]
print(casos_de_prueba[0]["nombre"], casos_de_prueba[1]["nombre"], casos_de_prueba[2]["nombre"])"""

prueba = {"chrome", "firefox", "chrome", "safari", "edge", "firefox"}
print(len(prueba))

tupla = ("admin", "1234")
print(tupla[0:2])