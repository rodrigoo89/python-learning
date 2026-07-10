def abrir_leer (archivo):
    archivo = open("ejemplo.txt", "r")
    contenido = archivo.read()
    archivo.close()
    return contenido