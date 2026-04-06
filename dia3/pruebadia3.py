texto = input("Escribe todo lo que quieras: ")
letras = input("Ingresa 3 letras: ")

texto_minuscula = texto.lower()
letras = letras.lower()
letras = list(letras)
texto_separado = texto.split()

print("Tu texto es: " + texto)
print("Tus letras son: " + str(letras))

contador1 = texto_minuscula.count(letras[0])
contador2 = texto_minuscula.count(letras[1])
contador3 = texto_minuscula.count(letras[2])

contador_palabras = len(texto_separado)
ultima_letra = texto[-1]
primera_letra = texto[0]

verificador = "python" in texto_minuscula
texto_invertido = texto_separado[::-1]
texto_invertido = " ".join(texto_invertido)

print(f"La letra '{letras[0]}' aparece {contador1} veces")
print(f"La letra '{letras[1]}' aparece {contador2} veces")
print(f"La letra '{letras[2]}' aparece {contador3} veces")

print(f"El texto tiene {contador_palabras} palabras")
print(f"La primera letra del texto es '{primera_letra}'")
print(f"La última letra del texto es '{ultima_letra}'")
print(f"La palabra 'python' se encuentra en el texto: {verificador}")
print(f"El texto invertido es: {texto_invertido}")