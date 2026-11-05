'''
Nivel 3: Retos

3.1: Calculadora
Crea calcular(a, operador, b) donde operador es "+", "-", "*" o "/".

Si el operador no es válido → "Operador inválido"
Si divide entre 0 → "No se puede dividir entre 0"
'''

def  calcular(a, operador, b):
    if b == 0:
        return "No se puede dividir entre 0"    
    elif operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        return a / b
    return "Operador inválido"

print(calcular(6, "%", 2))