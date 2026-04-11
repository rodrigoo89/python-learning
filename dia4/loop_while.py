monedas = 9

while monedas > 0: # El bucle `while` se ejecutará mientras la condición `monedas > 0` sea verdadera. En cada iteración, se restará 1 a la variable `monedas`, lo que simula el gasto de una moneda. Cuando `monedas` llegue a 0, la condición ya no será verdadera y el bucle se detendrá.
    print(f"Te quedan {monedas} monedas")
    monedas -= 1 # Esta línea de código es equivalente a `monedas = monedas - 1`. En cada iteración del bucle, se resta 1 a la variable `monedas`, lo que simula el gasto de una moneda. Al finalizar el bucle, `monedas` llegará a 0 y la condición del `while` ya no será verdadera, deteniendo la ejecución del bucle.
else:
    print("No te quedan monedas")  
    
 
#EJEMPLO DE USO DE `while` PARA UN JUEGO DE ADIVINANZAS
   
respuesta = "S"

while respuesta == "S":
    respuesta = input("¿Quieres seguir jugando? (S/N): ").upper() # La función `input()` se utiliza para solicitar al usuario que ingrese una respuesta. El método `upper()` convierte la respuesta a mayúsculas, lo que permite que el programa acepte tanto "S" como "s" como respuestas válidas para continuar el juego. Si el usuario ingresa "S", el bucle continuará ejecutándose; si ingresa "N" o cualquier otra cosa, el bucle se detendrá.
else:
    print("¡Gracias por jugar!")
    

nombre = input("¿Cuál es tu nombre? ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)
# En este código, se solicita al usuario que ingrese su nombre. Luego, se itera a través de cada letra del nombre utilizando un bucle `for`. Si la letra es "r", se utiliza la declaración `break` para salir inmediatamente del bucle, lo que significa que no se imprimirán las letras restantes después de la "r". Para todas las letras antes de la "r", se imprimirán normalmente. Al finalizar el bucle, si se encontró una "r", el programa habrá salido del bucle y no se imprimirán las letras posteriores a la "r".  
    

nombre = input("¿Cuál es tu nombre? ")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)
# En este código, se solicita al usuario que ingrese su nombre. Luego, se itera a través de cada letra del nombre utilizando un bucle `for`. Si la letra es "r", se utiliza la declaración `continue` para saltar esa iteración y no imprimir la letra "r". Para todas las demás letras, se imprimen normalmente. Al finalizar el bucle, se habrán impreso todas las letras del nombre excepto las "r".


numero = 10

while numero > 0:
     numero -=1
     print(numero)
     
     
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1
    
#Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)