mi_lista = ["a", "b", "c", "d", "e"]

for letra in mi_lista:
    numero = mi_lista.index(letra)
    print(f"La letra es: {letra} y su índice es: {numero    }")
    
    

lista = ["Pablo", "María", "Juan", "Ana","Julia"]

for nombre in lista:
    if nombre.startswith("J"):
        print(f"{nombre} empieza con J")
    else:
        print(f"Este {nombre} no empieza con J")
        
        
numeros = [1, 2, 3, 4, 5]
valor = 0

for numero in numeros:
    valor = valor + numero
print(f"La suma de los números es: {valor}")