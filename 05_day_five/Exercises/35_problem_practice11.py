'''
Ejercicio 4:

Escribe una función llamada contar_primos() que requiera un 
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números 
primos existentes en el rango que va desde cero hasta ese 
número incluido, y va a devolver la cantidad de números 
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
'''
def contar_primos():

    lista_primos = []

    for numero_actual in range(2,51):

        es_primo = True

        for divisor in range(2, numero_actual):
            if numero_actual % divisor == 0:
                es_primo = False
                break

        if es_primo:
            lista_primos.append(numero_actual)
    return lista_primos

print(contar_primos())