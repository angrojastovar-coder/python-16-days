'''
2.2: Fin de semana
Crea es_fin_de_semana(dia) que devuelva True para "sábado" o "domingo" (usa in).
'''

def es_fin_de_semana(dia):
    return dia in ("sabado", "domingo")

resultado = es_fin_de_semana("sabado")
print(resultado)