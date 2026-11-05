'''
Repaso: Avanzado

3.2: FizzBuzz
Crea fizzbuzz(n) que devuelva una lista del 1 al n donde:

múltiplos de 3 → "Fizz"
múltiplos de 5 → "Buzz"
múltiplos de ambos → "FizzBuzz"
los demás → el número
'''

def fizzbuzz(n):
    lista = []
    contador = 1

    while contador <= n:
        if contador % 3 == 0 and contador % 5 == 0:
            lista.append("FizzBuzz")
        elif contador % 5 == 0:
            lista.append("Buzz")
        elif contador % 3 == 0:
            lista.append("Fizz")
        else:
            lista.append(contador)
        contador += 1
    return lista

resultado = fizzbuzz(15)
print(resultado)