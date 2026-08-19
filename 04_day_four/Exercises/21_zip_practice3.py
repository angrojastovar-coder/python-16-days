'''
Práctica Zip 3: 
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés 
(en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable 
numeros:
    1. uno / um / one
    2. dos / dois / two
    3. tres / três / three
    4. cuatro / quatro / four
    5. cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
'''
spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]

numbers = list(zip(spanish, portuguese, english))
print(numbers)