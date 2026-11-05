'''
1.3: Par o impar
Crea par_o_impar(n) que devuelva "par" o "impar".
'''

def par_o_impar(n):
    if n % 2 == 0:
        return f"par"
    return f"impar"

resultado = par_o_impar(9)
print(resultado)