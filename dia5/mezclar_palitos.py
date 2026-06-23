from random import shuffle

palitos = ["=", "==", "===", "===="]

def mezclar_palitos(palitos):
    shuffle(palitos)
    return palitos

def probar_suerte():
    palito_elegido =  ""
    while palito_elegido not in ["1", "2", "3", "4"]:
        palito_elegido = input("Elija un palito (1-4): ")
    return int(palito_elegido) - 1

def chequear_palito(palitos, palito_elegido):
    if palitos[palito_elegido] == "====":
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
        
palitos = mezclar_palitos(palitos)      # mezcla los palitos
palito_elegido = probar_suerte()        # el jugador elige
chequear_palito(palitos, palito_elegido) # chequea si ganó o perdió
