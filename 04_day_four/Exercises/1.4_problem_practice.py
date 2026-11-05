'''
1.4: Contraseña
Crea contrasena_correcta(texto) que devuelva True solo si el texto es exactamente "python123".
'''

def contrasena_correcta(texto):
    return texto == "python123"

resultado = contrasena_correcta("python123")
print(resultado)