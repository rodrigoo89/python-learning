cliente = {"nombre": "Federico",
           "edad": 50,
           "ocupación": "instructor"}

pelicula = {"titulo": "Matrix",
            "ficha_técnica": {"protagonista": "Keanu Reeves",
                              "director": "Lana y Lily Wachowski"}}

libro = {"titulo": "1984",
         "autor": "George Orwell"}

elementos = [cliente, pelicula, libro]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupación": ocupacion}:
            print("este es un cliente")
            print(nombre, edad, ocupacion)

        case {"titulo": titulo,
              "ficha_técnica": {"protagonista": protagonista,
                                "director": director}}:
            print("esta es una película")
            print(titulo, protagonista, director)

        case _:
            print("No se que tipo de elemento es")
           