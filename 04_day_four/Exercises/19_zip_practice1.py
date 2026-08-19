'''
Práctica Zip 1:

Muestra en pantalla frases como la del siguiente ejemplo: La capital de Alemania es Berlín

Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo 
rápida y eficientemente.
    - capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
    - paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

'''

capital = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
countries = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
geo = zip(capital, countries)

for capital, country in geo:
    print(f"The capital of {country} is {capital}")