mi_lista = ["a", "b", "c", "d", "e"]

for letra in mi_lista:
    numero = mi_lista.index(letra)
    print(f"La letra es: {letra} y su índice es: {numero    }")
    
    

lista = ["Pablo", "María", "Juan", "Ana","Julia"]

for nombre in lista:
    if nombre.startswith("J"): #startswith es un método de las cadenas de texto que devuelve True si la cadena comienza con el prefijo especificado, y False en caso contrario.
        print(f"{nombre} empieza con J")
    else:
        print(f"Este {nombre} no empieza con J")
        
        
numeros = [1, 2, 3, 4, 5]
valor = 0

for numero in numeros: #En cada iteración del bucle, se toma el número actual de la lista "numeros" y se suma al valor acumulado en la variable "valor". Al finalizar el bucle, "valor" contendrá la suma total de todos los números en la lista.
    valor = valor + numero # Esta línea de código es la que realiza la suma acumulativa. En cada iteración, el número actual se agrega al valor acumulado en la variable "valor". Al finalizar el bucle, "valor" contendrá la suma total de todos los números en la lista "numeros".    
print(f"La suma de los números es: {valor}")

# Tipo de dato             | Ejemplo                           | Qué recorre el `for`            |
# ------------------------ | --------------------------------- | ------------------------------- |
# **string**               | `"hola"`                          | cada **letra**                  |
# **lista**                | `[10, 20, 30]`                    | cada **elemento**               |
# **tupla**                | `(1, 2, 3)`                       | cada **elemento**               |
# **diccionario**          | `{"nombre": "Rodri", "edad": 30}` | cada **clave**                  |
# **diccionario.values()** | `dic.values()`                    | cada **valor**                  |
# **diccionario.items()**  | `dic.items()`                     | **clave y valor**               |
# **set**                  | `{1, 2, 3}`                       | cada **elemento**               |
# **range()**              | `range(5)`                        | cada **número** de la secuencia |

# Ejemplo de uso de `for` con diferentes tipos de datos
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print(f"Hola {nombre}")
  
# Ejemplo de uso de `for` con un diccionario    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
   suma_numeros += numero


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num
# En este código, se itera a través de cada número en la lista "lista_numeros". Si el número es par (es decir, si el residuo de la división por 2 es 0), se suma al acumulador "suma_pares". Si el número es impar, se suma al acumulador "suma_impares". Al finalizar el bucle, se imprimen los resultados de ambas sumas.
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")