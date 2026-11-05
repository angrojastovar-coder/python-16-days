'''
Repaso: Avanzado

3.4: Detective de errores 🔎
Esta función debería sumar todos los elementos, pero con [1, 2, 3] devuelve 1. ¿Por qué? ¿Cómo la arreglas?
'''

def suma_lista(lista):
    total = 0
    for n in lista:
        total += n
        return total

resultado = suma_lista([1, 2, 3])
print(resultado) 

'''
Esta funcion solo suma 1 porque el returno se encuentra dentro del for
cuando hace la primera iteración llega al return y se acaba por eso solo 
termina sumando el 1. Si re corre la sangria si realizaría toda la suma.
'''
    