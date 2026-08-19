texto = input("¿Puedes ingresar un texto por favor? No importa el tamaño. ").lower()

letras = list(input("Adicional, puedes ingresar 3 letras diferentes? Nota: no agregues espacios entre ellas ").lower())

letra_uno = texto.count(letras[0])
letra_dos = texto.count(letras[1])
letra_tres = texto.count(letras[2])

print(f"La letra '{letras[0]}' aparece {letra_uno}")
print(f"La letra '{letras[1]}' aparece {letra_dos}")
print(f"La letra '{letras[2]}' aparece {letra_tres}")

#2. Cuantas palabras hay a lo largo del texto
separar = texto.split(" ") #Separar por espacios.
texto_list = list(separar) 
tam_texto = len(texto_list) #Contar el numero de palabras
print(f"A lo largo del texto se encuentran {tam_texto} palabras") #Print con la informacion

#Cual es la primera y la ultima letra del texto
print(f"El último caracter del texto es: {texto[0]}") #Indexación, primer caracter del texto ingresado
print(f"El última caracter del texto es: {texto[-1]}") #Indexación, último caracter del texto ingresado

#Invertir orden de las palabras
texto_list.reverse()
print(f"Así quedaría el texto si revirtieramos su orden: {texto_list}")

#Unir los elementos con espacios intermedios
unir = " ".join(texto_list) #Unir varios elementos de una lista por un elemento que se indique
print(f"Si llegamos a unir todas las palabras en un solo texto, queda así: {unir}")

#Está la palabra Python en el texto? / #diccionario
palabra = "python" in texto
palabra_clave = {True: "La palabra python está dentro de tu texto. Pero TODA en minuscula, ¡Qué cool!"}
frase_final = palabra_clave.get(palabra, "No tienes la palabra Python dentro de tu texto")
print(frase_final)