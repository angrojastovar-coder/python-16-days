from random import *

name = input("Hola, ¿cual es tu nombre?: ")
print(f"Bueno, {name}, he pensado un número entre 1 y 100.\nTienes solo ocho intentos para adivinar")

print("\n")

intentos = 0
secreto = randint(1,100)

while intentos < 8:
    adivina = int(input(f"Intento {intentos + 1} - ¿Cúal crees que es el número?: "))
    intentos += 1

    if adivina < 1 or adivina > 100:
        print("El número que ingresaste está fuera del rango, recuerda que es entre 1 y 100")
    elif adivina < secreto:
        print("El número que ingresaste es incorrecto, elegiste un número menor al número secreto")
    elif adivina > secreto:
        print("El número que ingresaste es incorrecto, elegiste un número mayor al número secreto")
    elif adivina == secreto:
        print(f"Haz acertadoo!!! El número que ingresaste es correcto y te tomó {intentos} intentos")
        break
else:
    print(f"{name} se acabaron los intentos, el número era {secreto}")