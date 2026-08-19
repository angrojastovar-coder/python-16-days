pasos = ["abrir app", "ingresar usuario", "ingresar clave", "click login"]
pasos.insert(1, "aceptar términos")
print(pasos[-2:])
pasos.remove("click login")
print(pasos)