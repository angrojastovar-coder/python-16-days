'''
Nivel 3: Retos

3.1: Ticket de compra
Crea variables para producto, precio (float) y cantidad (int). Calcula el subtotal, el IVA del 19% y el total. 
Muestra todo con dos decimales:
'''

producto = "Pan"
precio = 1000
cantidad = 15
subtotal = precio * cantidad
iva = subtotal * 0.19
total = subtotal + iva

print(f"producto, {subtotal:.2f}, {iva:.2f}, {total:.2f}")

