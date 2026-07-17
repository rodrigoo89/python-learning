import pygame
import random


def posicion_random_borde():
    # Elige un borde al azar y devuelve una posición (x, y) sobre ese borde
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    if borde == "arriba":
        return random.randint(0, 800 - 54), 0
    elif borde == "abajo":
        return random.randint(0, 800 - 54), 600 - 64
    elif borde == "izquierda":
        return 0, random.randint(0, 600 - 64)
    else:  # derecha
        return 800 - 54, random.randint(0, 600 - 64)


class Enemigo:
    # Clase base para los enemigos que persiguen al repartidor. Cada
    # subclase (Perro, Gato, etc.) solo debe definir su propia imagen
    # (atributo de clase, compartida por todas las instancias) y su
    # propia velocidad; el resto del comportamiento es común.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_hacia(self, objetivo_x, objetivo_y):
        # Avanza en línea recta hacia (objetivo_x, objetivo_y), a la
        # velocidad propia de la subclase (Pitágoras: dx, dy, distancia).
        dx = objetivo_x - self.x
        dy = objetivo_y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        if distancia != 0:  # Evitar división por cero si ya está encima
            self.x += (dx / distancia) * self.velocidad
            self.y += (dy / distancia) * self.velocidad

    def dibujar(self,pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def rect(self):
        # Rect real (posición + tamaño de la imagen), para usar con colliderect
        return pygame.Rect(self.x, self.y, self.imagen.get_width(), self.imagen.get_height())
