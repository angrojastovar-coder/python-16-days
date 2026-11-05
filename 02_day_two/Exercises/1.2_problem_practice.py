'''
Nivel 2: Calentando motores

2.2: Calculadora de propina
Pide el valor de una cuenta (float) y calcula una propina del 10%. Muestra la cuenta, la propina y el total.
'''

valor_cuenta = float(input("Ingresa el valor de la cuenta: "))
propina = valor_cuenta * 0.1
total = valor_cuenta + propina
print(valor_cuenta, int(propina), int(total))