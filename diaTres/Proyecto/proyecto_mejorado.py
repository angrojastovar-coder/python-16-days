texto = input("¿Puedes ingresar un texto por favor? No importa el tamaño: ").lower()
letras = []

print("\n")

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

letra_uno = texto.count(letras[0])
letra_dos = texto.count(letras[1])
letra_tres = texto.count(letras[2])

print("\n")
print("CANTIDAD DE LETRAS EN EL TEXTO")

print(f"La letra '{letras[0]}' aparece {letra_uno} veces en el texto")
print(f"La letra '{letras[1]}' aparece {letra_dos} veces en el texto")
print(f"La letra '{letras[2]}' aparece {letra_tres} veces en el texto")

print("\n")
print("CANTIDAD DE PALABRAS EN EL TEXTO")

#2. Cuantas palabras hay a lo largo del texto
palabras_list = texto.split() #Separar por espacios y convertir el str en una lista.
print(f"A lo largo del texto se encuentran {len(palabras_list)} palabras") #Print con la informacion

print("\n")
print("PRIMERA Y ULTIMA LETRA EN EL TEXTO")

#Cual es la primera y la ultima letra del texto
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"El último caracter del texto es: {letra_inicio}") #Indexación, primer caracter del texto ingresado
print(f"El última caracter del texto es: {letra_final}") #Indexación, último caracter del texto ingresado

print("\n")
print("TEXTO INVERTIDO")

#Invertir orden de las palabras
palabras_list.reverse()
#Unir los elementos con espacios intermedios
texto_invertido_unido = " ".join(palabras_list) #Unir varios elementos de una lista por un elemento que se indique
print(f"El texto invertido va a quedar así: {texto_invertido_unido}")

print("\n")
print("PALABRA PYTHON EN EL TEXTO")

#Está la palabra Python en el texto? / #diccionario
buscar_palabra = "python" in texto
palabra_clave = {True: "si", False: "no"}
print(f"La palabra 'python'{palabra_clave[buscar_palabra]} se encuentra en el texto")