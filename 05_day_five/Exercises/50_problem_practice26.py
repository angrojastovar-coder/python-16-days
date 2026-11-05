'''
Repaso: Calentamiento

Ejercicio 2.4: Clasificar nota
Crea clasificar(nota):

90 o más → "Excelente"
70 a 89 → "Aprobado"
menos de 70 → "Reprobado"
'''

def calificar(nota):
    if nota >= 90:
        return f"Excelente"
    if nota >= 70:
        return f"Aprobado"
    return f"Reprobado"

nota = calificar(20)
print(nota)