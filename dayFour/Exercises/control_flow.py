"""num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")"""


edad = 18
tiene_licencia = True

if edad >= 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
     print("Puedes conducir")