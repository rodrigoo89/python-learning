import pygame


class Repartidor:
    # El personaje que maneja el jugador. Se mueve con las flechas, es el
    # origen de las pizzas y tiene vidas con un período de invulnerabilidad
    # tras cada golpe recibido.
    imagen = pygame.transform.scale(pygame.image.load("image/repartidor.png"), (64, 100))  # Una sola vez, compartida por todas las instancias
    velocidad = 1
    ancho_pantalla = 800
    alto_pantalla = 600
    duracion_invulnerabilidad = 1000  # Milisegundos de invulnerabilidad tras perder una vida

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_cambio = 0  # Movimiento horizontal según las teclas apretadas
        self.y_cambio = 0  # Movimiento vertical según las teclas apretadas
        self.vidas = 3
        self.invulnerable_hasta = 0  # Timestamp (ms) hasta el cual es invulnerable

    def mover(self):
        self.x += self.x_cambio
        self.y += self.y_cambio

        # Límites de pantalla para que no se salga
        if self.x < 0:
            self.x = 0
        if self.x > self.ancho_pantalla - self.imagen.get_width():
            self.x = self.ancho_pantalla - self.imagen.get_width()
        if self.y < 0:
            self.y = 0
        if self.y > self.alto_pantalla - self.imagen.get_height():
            self.y = self.alto_pantalla - self.imagen.get_height()

    def es_invulnerable(self, tiempo_actual):
        return tiempo_actual < self.invulnerable_hasta

    def perder_vida(self, tiempo_actual):
        self.vidas -= 1
        self.invulnerable_hasta = tiempo_actual + self.duracion_invulnerabilidad

    def rect(self):
        # Rect real (posición + tamaño de la imagen), para usar con colliderect
        return pygame.Rect(self.x, self.y, self.imagen.get_width(), self.imagen.get_height())

    def dibujar(self, pantalla, tiempo_actual):
        # Mientras es invulnerable, parpadea (se dibuja solo la mitad de los frames)
        if not self.es_invulnerable(tiempo_actual) or (tiempo_actual // 100) % 2 == 0:
            pantalla.blit(self.imagen, (self.x, self.y))
