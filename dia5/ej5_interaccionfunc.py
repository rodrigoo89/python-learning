def reducir_lista(lista):
    unicos = list(set(lista))
    unicos.remove(max(unicos))
    return unicos

def promedio(lista):
    return sum(lista) / len(lista)


# Variable de ejemplo
lista_numeros = [1, 2, 15, 7, 2]