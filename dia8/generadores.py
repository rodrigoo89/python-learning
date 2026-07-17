def mi_funcion():
    lista=[]
    for x in range(5):
        lista.append(x)
    return lista

def mi_generador():
    for x in range(5):
        yield x

print(mi_funcion())
print(mi_generador())

g=mi_generador()
print(next(g))


def crear_generador():
    num = 1 
    while True:
        yield num
        num += 1

generador = crear_generador()
print(next(generador))


def crear_generador():
    num = 3  # arrancamos con 3 vidas
    while num > 0:
        # mientras queden vidas, entregamos el mensaje con la cantidad actual
        yield (f"Te quedan {num} vidas" if num > 1 else f"Te queda {num} vida")
        num -= 1
    # cuando el while termina (num llegó a 0), entregamos el último mensaje
    yield "Game Over"

perder_vida = crear_generador()

print(next(perder_vida))  # Te quedan 3 vidas
print(next(perder_vida))  # Te quedan 2 vidas
print(next(perder_vida))  # Te queda 1 vida
print(next(perder_vida))  # Game Over
