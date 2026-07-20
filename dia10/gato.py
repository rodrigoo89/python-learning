import pygame
from enemigo import Enemigo, posicion_random_borde

class Gato(Enemigo):
    imagen = pygame.transform.scale(pygame.image.load("image/gato.png"), (42, 52))  # Una sola vez, compartida por todos los gatos
    velocidad = 0.9

    def __init__(self):
        x, y = posicion_random_borde()
        super().__init__(x, y)