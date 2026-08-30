'''
Ejercicio 3: El cazador de palabras cortas

- Objetivo: Crear una función que reciba una lista de palabras y devuelva 
una nueva lista que contenga solo las palabras que tengan menos de 5 letras.
- Pista: Para crear una lista vacía usa resultado = []. Para medir una palabra
usa len(palabra). Para agregar elementos a la lista nueva usa resultado.append(palabra).
- Lista de prueba: ["sol", "computadora", "gato", "azul", "elefante"] 
(Debe devolver ["sol", "gato", "azul"]).
'''

palabras = ["sol", "computadora", "gato", "azul", "elefante"]

def lista_palabras(lista):
    resultado = []
    for i in lista:
        if len(i) < 5:
            resultado.append(i)
    return resultado

resultado = lista_palabras(palabras)
print(resultado)