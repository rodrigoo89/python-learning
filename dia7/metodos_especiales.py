class CD:
    
    def __init__(self, autor, titulo, nro_canciones):
        self.titulo = titulo
        self.autor = autor
        self.nro_canciones = nro_canciones
    
    def __str__(self):
        return f"CD: {self.titulo} - Autor: {self.autor} - Nro de canciones: {self.nro_canciones}"
    
    def __len__(self):
        return self.nro_canciones
    
    def __del__(self):
        print(f"El CD  ha sido eliminado.")

cd_1 = CD("Metallica", "Master of Puppets", 8)

print(cd_1)
del cd_1  # Esto llamará al método __del__ y mostrará el mensaje de eliminación

print(cd_1)  # Esto generará un error porque cd_1 ha sido eliminado



class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
    
    
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print(f"Libro eliminado.")