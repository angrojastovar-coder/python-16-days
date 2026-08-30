'''
Ejercicio 4: El filtro estricto de sueldos

- Objetivo: Crear una función que reciba una lista de salarios. 
Debe calcular la suma de los salarios, pero excluyendo los que sean 
menores a 1000 O mayores a 5000 (es decir, solo sumas los que están entre 
1000 y 5000 inclusive).
- Pista: Es muy parecido al que acabas de resolver, pero usando >= y <=.
- Lista de prueba: [900, 1500, 3000, 6000, 2000] (Debe dar como resultado 6500).
'''

lista_salarios = [900, 1500, 3000, 6000, 2000]

def salarios(lista):
    suma = 0
    for i in lista:
        if i >= 1000 and i <= 5000:
            suma = suma + i
    return suma

resultado = salarios(lista_salarios)
print(resultado)