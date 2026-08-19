nombre = input("¿Cómo te llamas?: ")
monto = float(input("¿Cuanto has vendido en este mes?: "))
comisiones = round((monto * 13) / 100,2)
print(f"""Hola {nombre}, este mes alcanzaste un total de ventas de 
      {monto}. De acuerdo a ese monto, tu comision para este mes es de {comisiones}""")