'''
Práctica Enumerador 3:

Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, 
que empiecen con M:
    - lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", 
    "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos 
de los siguientes elementos:
    - Loops
    - Condicionales if
    - El método enumerate()
    - Métodos de strings o indexado
'''

lista_nombres = enumerate(["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"])

for index, nombre in lista_nombres:
    if nombre[0] == "M":
        print(f"El nombre en el indice {index} empieza con letra M")
    else:
        continue