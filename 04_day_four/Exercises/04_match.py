cliente = {"nombre" : "Angela", 
           "edad": 27,
           "ocupación": "Automation QA"}
pelicula = {"titulo":"Matrix",
            "ficha técnica":{"protagonista": "Keanu Reeves",
                             "director": "Lana y Lily Wachowski"}}
libro = {"titulo": "1984",
         "autor": "George Orwell"}

elementos = [cliente, pelicula, libro]

for e in elementos:
    match e:
        case {"nombre" : nombre, 
           "edad": edad,
           "ocupación": ocupacion}:
            print("Este es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo": titulo,
            "ficha técnica":{"protagonista": protagonista,
                             "director": director}}:
            print("Esta es una película")
            print(titulo, protagonista, director)
        case _:
            print("No sé que sea")