bug = {"id": 101, "titulo": "Botón no responde", "severidad": "alta"}
print(bug.get("asignado_a","sin asignar"))
bug["asignado_a"] = "Angela"
print(bug)
print(bug.pop("severidad"))