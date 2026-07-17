import pygame


class Interfaz:
    # Agrupa todo lo que el jugador ve en pantalla aparte de los objetos del
    # juego: puntaje, cronómetro, corazones de vida y el cartel de fin de
    # juego. No conoce ni modifica el estado del juego, solo lo dibuja a
    # partir de los datos (puntaje, vidas, tiempo) que le pasan.
    corazon_img = pygame.transform.scale(pygame.image.load("image/corazon.png"), (32, 32))  # Una sola vez, compartida

    def __init__(self):
        self.fuente = pygame.font.Font(None, 36)  # Fuente para puntaje, cronómetro y game over
        self.fuente_grande = pygame.font.Font(None, 72)  # Fuente para el texto "GAME OVER"

    def mostrar_puntaje(self, pantalla, puntaje):
        texto_puntaje = self.fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))  # Color blanco
        pantalla.blit(texto_puntaje, (650, 10))  # Posición del puntaje en la pantalla

    def mostrar_vidas(self, pantalla, vidas):
        for i in range(vidas):
            pantalla.blit(self.corazon_img, (10 + i * 36, 10)) # Posición de los corazones en la pantalla, separados por 36 píxeles

    def formatear_tiempo(self, tiempo_ms):
        # Convierte milisegundos a un string "M:SS"
        minutos = tiempo_ms // 60000
        segundos = (tiempo_ms // 1000) % 60
        return f"{minutos}:{segundos:02d}"

    def mostrar_cronometro(self, pantalla, tiempo_transcurrido_ms):
        # Renderiza el cronómetro centrado arriba de la pantalla
        texto_tiempo = self.fuente.render(f"Tiempo: {self.formatear_tiempo(tiempo_transcurrido_ms)}", True, (255, 255, 255))
        rect_tiempo = texto_tiempo.get_rect(center=(400, 20))
        pantalla.blit(texto_tiempo, rect_tiempo)

    def mostrar_pantalla_final(self, pantalla, puntaje, tiempo_transcurrido_ms):
        # Dibuja el cartel de fin de juego: fondo semitransparente + GAME OVER + puntaje + tiempo
        overlay = pygame.Surface((500, 200), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        pantalla.blit(overlay, (150, 200))

        texto_game_over = self.fuente_grande.render("GAME OVER", True, (0, 0, 0))
        rect_game_over = texto_game_over.get_rect(center=(400, 250))
        pantalla.blit(texto_game_over, rect_game_over)

        texto_puntaje_final = self.fuente.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
        rect_puntaje_final = texto_puntaje_final.get_rect(center=(400, 310))
        pantalla.blit(texto_puntaje_final, rect_puntaje_final)

        texto_tiempo_final = self.fuente.render(f"Tiempo sobrevivido: {self.formatear_tiempo(tiempo_transcurrido_ms)}", True, (0, 0, 0))
        rect_tiempo_final = texto_tiempo_final.get_rect(center=(400, 350))
        pantalla.blit(texto_tiempo_final, rect_tiempo_final)
