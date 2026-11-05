'''
Repaso: Avanzado

1.3: Suma y promedio
Crea suma_y_promedio(lista) que devuelva dos valores.
'''

def suma_y_promedio(lista):
    suma = 0

    for n in lista:
        suma += n
        promedio = suma / len(lista)
    return suma, promedio

resultado_suma, resultado_promedio = suma_y_promedio([2, 4, 6])
print(resultado_suma,resultado_promedio)