registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
mi_archivo = open("registro.txt", "a")
mi_archivo.write("\t".join(registro_ultima_sesion))
mi_archivo.close()

mi_archivo = open("registro.txt", "r")
print(mi_archivo.read())
mi_archivo.close()