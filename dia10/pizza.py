import pygame


class Pizza:
    # La pizza que dispara el repartidor. Se crea apuntando hacia un objetivo
    # (el enemigo más cercano) y a partir de ahí viaja en línea recta con la
    # dirección (dx, dy) calculada una sola vez al lanzarla.
    imagen = pygame.transform.scale(pygame.image.load("image/pizza.png"), (32, 32))  # Una sola vez, compartida por todas las pizzas
    velocidad = 1.6

    def __init__(self, x, y, objetivo_x, objetivo_y):
        self.x = x
        self.y = y
        dx = objetivo_x - x
        dy = objetivo_y - y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        if distancia != 0:  # Evitar división por cero si se lanza sin objetivo
            self.dx = (dx / distancia) * self.velocidad
            self.dy = (dy / distancia) * self.velocidad
        else:
            self.dx, self.dy = 0, self.velocidad

    def mover(self):
        self.x += self.dx
        self.y += self.dy

    def dentro_de_pantalla(self, ancho=800, alto=600):
        return 0 <= self.x <= ancho and 0 <= self.y <= alto

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def rect(self):
        # Rect real (posición + tamaño de la imagen), para usar con colliderect
        return pygame.Rect(self.x, self.y, self.imagen.get_width(), self.imagen.get_height())
