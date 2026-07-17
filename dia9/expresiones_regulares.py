import re

texto = " si necesitas ayuda llama al (249).454.9876 las 24 horas del dia"

patron = "ayuda"
busqueda = re.search(patron, texto)
print(busqueda)


texto1= "llama al 555-123-2345 ya mismo"
patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto1)
print(resultado)



clave= input("Ingrese la clave: ")
patron = r"\D{1}\w{3}"

resultado = re.search(patron, clave)
print(resultado)