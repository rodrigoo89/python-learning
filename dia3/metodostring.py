texto = "Este es el texto de Rodrigo"

resultado = texto.upper()# Devuelve el texto en mayúsculas
resultado1 = texto.lower()# Devuelve el texto en minúsculas
resultado2 = texto.split()# Devuelve una lista de palabras del texto, separadas por espacios
resultado3 = texto.find("Rodrigo")# Devuelve la posición de la primera aparición de "Rodrigo" en el texto, o -1 si no se encuentra
resultado4 = texto.replace("Rodrigo", "Juan")# Devuelve una nueva cadena de texto donde todas las apariciones de "Rodrigo" han sido reemplazadas por "Juan"
print(resultado)    
print(resultado1)   
print(resultado2)  
print(resultado3)  
print(resultado4)  

a = "Aprender"
b= "Python"
c= "es"
d= "divertido"
e= "".join([a, b, c, d])# Devuelve una nueva cadena de texto que es la concatenación de las cadenas a, b, c y d, sin espacios entre ellas
print(e)    


#lista_palabras = ["La","legibilidad","cuenta."]
#print(" ".join(lista_palabras))

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

eliminado = frutas.pop(2)

print(eliminado)