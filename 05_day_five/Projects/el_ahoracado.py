from random import *
import string

# Elegir palabra
def elegir_palabra(palabras_juego):
    
    palabra_elegida = choice(palabras_juego)
    return (palabra_elegida)

# Mostrar cada uno de los guiones por letra de la palabra

def mostrar_guiones_palabra(palabra_elegida):

    guiones_letras = []

    for letra in palabra_elegida:
        
        if letra == " ":
            guiones_letras.append(" ")
        else:
            guiones_letras.append("_")
    return guiones_letras

# Solicitar al usuario que ingrese una letra

def pedir_letra_al_usuario():
        letra = input("Ingresa una letra, valida que esté correcta o que no la hayas ingresado antes: ").lower()
        return letra

# Validar que el dato ingresado si sea una letra y no otro tipo de dato

def validar_tipo_dato(letra_ingresada, letras_ingresadas):

    letras_validas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    while letra_ingresada not in letras_validas or letra_ingresada in letras_ingresadas:
        letra_ingresada = pedir_letra_al_usuario()

    letras_ingresadas.append(letra_ingresada)

    return letra_ingresada

# Validar que la letra ingresada por el usuario si esté dentro de la palabra elegida al azar

def validar_letra(letra_ingresada, palabra_elegida, guiones_palabra, letras_ingresadas):

    vidas = len(guiones_palabra)

    while vidas > 0:
        if letra_ingresada in palabra_elegida and len(letra_ingresada) == 1:
            print("Acertaste")

            for posicion, letra_real in enumerate(palabra_elegida):
                if letra_ingresada == letra_real:
                    guiones_palabra[posicion] = letra_ingresada
            print(guiones_palabra)
        
            if "".join(guiones_palabra) == palabra_elegida:
                print(f"Lograste adivinar toda la palabra:")
                break           
        else:
            vidas = vidas - 1
            print(f"Ingresa solo una letra, te quedan: {vidas} vidas.")

            if vidas == 0:
                print(f"Te quedaste sin vidas. La palabra era '{palabra_elegida}'")
                break
        letra_ingresada = validar_tipo_dato(pedir_letra_al_usuario(), letras_ingresadas)
    return "".join(guiones_palabra)

def juego():

    palabras_juego = ["fido", "manzana", "aguila", "bugambilia", "copa de oro", "el espinal"]

    # Elegir palabra al azar
    palabra_elegida = elegir_palabra(palabras_juego)

    # Mostrar guiones para la palabra seleccionada
    palabra_guiones = mostrar_guiones_palabra(palabra_elegida)
    print(palabra_guiones)

    letras_ingresadas = []

    # Validar si el dato ingresado es válido como letra
    letra_usuario = pedir_letra_al_usuario()
    letra_verificada = validar_tipo_dato(letra_usuario, letras_ingresadas)

    # Validar si la letra está o no en la palabra
    print(validar_letra(letra_verificada, palabra_elegida, palabra_guiones, letras_ingresadas))
        
juego()