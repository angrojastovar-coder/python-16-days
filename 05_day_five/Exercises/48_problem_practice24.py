'''
Repaso: Calentamiento

Ejercicio 2.2: Saludo con valor por defecto
Crea saludar(nombre, saludo="Hola").
'''

def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

saludo = saludar("Gigi")
print(saludo)
saludo = saludar("Gigi","Buenas")
print(saludo)