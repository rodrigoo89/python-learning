def sobreescribir (archivo):
    archivo= open("ejemplo.txt", "w")
    archivo.write("contenido eliminado")
    archivo.close()
