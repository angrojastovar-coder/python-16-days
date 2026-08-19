#Ejercicio 1 -> Lista letras

'''list_letters = ["a", "b", "c"]

for element in list_letters:
    index_num = list_letters.index(element)
    print(f"This is the letter: {element} and has the next index {index_num}")'''

#Ejercicio 2 -> Lista nombres

'''People = ["Ana", "Brayan", "Lorena", "Daniela", "Valeria", "Roman"]

for name in People:
    if name.startswith("L"): 
        print(f"Your name start with letter 'L': {name}")
    else:
        print(f"Your name not start with letter 'L', but start with letter {name[0]}': {name}")'''

#Ejercicio 3

nums =  [1 , 2 , 3, 4, 5]
valor = 0

for num in nums:
    valor = valor + num
    print(valor)
print(valor)