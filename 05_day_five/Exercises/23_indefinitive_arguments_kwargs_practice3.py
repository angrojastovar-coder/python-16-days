'''
Práctica sobre Argumentos Indefinidos (**kwargs) 3:

Crea una función llamada describir_persona, que tome como parámetros su
nombre y luego una cantidad indetermida de argumentos. Esta función deberá
mostrar en pantalla:

    Características de {nombre}:
    {nombre_argumento}: {valor_argumento}
    {nombre_argumento}: {valor_argumento}
    etc...

Por ejemplo:
describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

    Características de María:
    color_ojos: azules
    color_pelo: rubio

No llames a la función, solamente definela sin llamarla."
'''

def describir_persona(nombre, **kwargs):
            mensaje = f"Características de {nombre}\n"

            for llave, valor in kwargs.items():
                    mensaje += f"{llave}: {valor}"
            return mensaje

print(describir_persona(nombre="María", color_ojos="azules", color_pelo="rubio"))
