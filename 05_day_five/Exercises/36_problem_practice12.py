'''
El Ejercicio: El Buscador de Letras Secretas (Anagramas cortos)

Imagina que tienes una lista de palabras. Quieres recorrer esa lista 
y encontrar cuáles palabras contienen TODAS las letras de una palabra secreta
(por ejemplo, la palabra secreta "sol").Si la palabra es "soldado", ¿tiene la 
s, la o y la l? ¡Sí! Pasa la prueba.Si la palabra es "sopa", ¿tiene la s, la o y
la l? No, le falta la l. No pasa.
'''

def adivinar_palabra(palabras):

    palabra_secreta = "sol"
    letras_encontradas = []

    for palabra_actual in palabras:

        coincide = True

        for letra in palabra_secreta:
            if letra not in palabra_actual:
                coincide = False
                break

        if coincide:
            letras_encontradas.append(palabra_actual)

    return f"Pasa la prueba, las letras encontradas son: {letras_encontradas}"

print(adivinar_palabra(["soldado", "sopa", "caracol", "solución", "luna"]))