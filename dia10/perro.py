import pygame
from enemigo import Enemigo, posicion_random_borde

class Perro(Enemigo):
    imagen = pygame.transform.scale(pygame.image.load("image/perro.png"), (54, 64))  # Una sola vez, compartida por todos los perros
    velocidad = 0.5

    def __init__(self):
        x, y = posicion_random_borde()
        super().__init__(x, y)
        
