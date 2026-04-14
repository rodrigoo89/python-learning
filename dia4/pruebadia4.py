from random import *

usuario = input("Ingrese su nombre: ")
print(f"Hola, {usuario}! Tendrás que adivinar un número entre 1 y 100. Tienes 8 intentos.")

numero_secreto = randint(1, 100)
intentos = 8

while intentos > 0:
    ingreso_numero = int(input(f"Te quedan {intentos} intentos. Ingresa un número: "))

    if ingreso_numero < 1 or ingreso_numero > 100:
        print("Por favor, ingresa un número entre 1 y 100.")
    elif ingreso_numero == numero_secreto:
        print(f"¡Felicidades, {usuario}! Has adivinado el número secreto en {9 - intentos} intentos.")
        break
    elif ingreso_numero < numero_secreto:
        print("Tu respuesta es incorrecta. Has elegido un número menor al número secreto.")
    else:
        print("Tu respuesta es incorrecta. Has elegido un número mayor al número secreto.")

    intentos -= 1

if intentos == 0:
    print(f"Lo siento, {usuario}. Has agotado tus intentos. El número secreto era {numero_secreto}.")