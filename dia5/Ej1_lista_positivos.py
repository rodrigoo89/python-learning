lista_numeros = [10,-20,30]
def todos_positivos (listanumeros): # función que recibe una lista de números y devuelve True si todos son positivos, False si encuentra alguno negativo
    for ln in listanumeros: # recorre la lista de números
        if ln <0: # si encuentra un número negativo, devuelve False
            return False
    return True                  # si terminó sin encontrar ninguno → True

