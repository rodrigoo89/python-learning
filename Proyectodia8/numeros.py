def agregar_texto(funcion_generadora):
    def envoltura():
        generador_original = funcion_generadora()
        while True:
            codigo = next(generador_original)
            yield f"Su turno es {codigo}. Aguarde y será atendido"
    return envoltura

@agregar_texto
def perfumeria():
    num = 1
    while True:
        yield f"P-{num}"
        num += 1

@agregar_texto
def farmacia():
    num = 1
    while True:
        yield f"F-{num}"
        num += 1

@agregar_texto
def cosmeticos():
    num = 1
    while True:
        yield f"C-{num}"
        num += 1