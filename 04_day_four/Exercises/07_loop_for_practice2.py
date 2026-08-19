'''
Práctica Loop For 2:

Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops
 For y almacena el resultado de la suma en una variable llamada suma_numeros:
    - lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
'''
list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
addition_numbers = 0

for num in list_numbers:
    addition_numbers = addition_numbers + num
print(addition_numbers)
