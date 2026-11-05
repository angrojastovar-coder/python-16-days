'''
Práctica sobre Interacción entre Funciones 3:

Crea una función (llamada lanzar_moneda) que devuelva el resultado de 
lanzar una moneda (al azar). Dicha función debe poder devolver los resultados
 "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el
primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento,
será una lista de números cualquiera (debes crear una lista con valores y llamarla
lista_numeros).
    - Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La 
    lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
    - Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue 
    salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al
azar de una secuencia.
'''
from random import *

def lanzar_moneda():
    moneda_al_aire = choice(["Cara", "Cruz"])
    return moneda_al_aire

def probar_suerte(resultado, lista):
    if resultado == "Cara":
        lista.clear()
        return(f"La lista se autodestruirá {lista}") 
    elif resultado ==  "Cruz":
        return(f"La lista fue salvada {lista}")
         

resultado = lanzar_moneda()
print(resultado)

lista_numeros = [1, 2, 3, 4, 5]
suerte = probar_suerte(resultado, lista_numeros.copy())
print(suerte)