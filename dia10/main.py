import pygame
import random
# Inicializamos Pygame
pygame.init()
pygame.mixer.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Game")  # Título de la ventana
icono = pygame.image.load("image/pizza.png")  # Cargar el ícono
pygame.display.set_icon(icono)  # Establecer el ícono de la ventana

# Fondo
fondo = pygame.image.load("image/fondo.png")  # Cargar la imagen de fondo
fondo = pygame.transform.scale(fondo, (800, 600))  # Ajustar el tamaño del fondo a la pantalla

# Repartidor
repartidor_img = pygame.image.load("image/repartidor.png")  # Cargar la imagen del repartidor
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100))  # Ajustar el tamaño del repartidor
repartidor_x = 368  # Posición inicial en el eje X
repartidor_y = 460  # Posición inicial en el eje Y
repartidor_x_cambio = 0  # Variable para controlar el movimiento horizontal del repartidor
repartidor_y_cambio = 0  # Variable para controlar el movimiento vertical del repartidor
velocidad_repartidor = 1  # Velocidad de movimiento del repartidor

# Perro
cantidad_perros = 2  # Cambiás este número para ajustar la cantidad de perros en juego

# Puntaje
puntaje = 0  # Inicializamos el puntaje en cero
fuente = pygame.font.Font(None, 36)  # Fuente para mostrar el puntaje
fuente_grande = pygame.font.Font(None, 72)  # Fuente para el texto "GAME OVER"
tiempo_inicio= pygame.time.get_ticks()  # Momento en que empieza el juego, para calcular tiempo transcurrido y mostrarlo en pantalla

# Estado del juego: "jugando" mientras se puede seguir jugando, "terminado" cuando se acaban las vidas
estado_juego = "jugando"
tiempo_final = 0  # Tiempo transcurrido (ms) en el momento exacto en que termina el juego, queda fijo

# Sonido
pygame.mixer.music.load("music/MusicaFondo.mp3")  # Música de fondo
pygame.mixer.music.set_volume(0.3)  # Volumen bajo para no tapar los efectos
pygame.mixer.music.play(-1)  # Loop infinito

sonido_disparo = pygame.mixer.Sound("music/disparo.mp3")
sonido_disparo.set_volume(0.7)
sonido_golpe = pygame.mixer.Sound("music/golpe.mp3")
sonido_golpe.set_volume(0.7)
sonido_vida_perdida = pygame.mixer.Sound("music/vida_perdida.mp3")
sonido_vida_perdida.set_volume(0.7)


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

    def dibujar(self):
        pantalla.blit(self.imagen, (self.x, self.y))

    def rect(self):
        # Rect real (posición + tamaño de la imagen), para usar con colliderect
        return pygame.Rect(self.x, self.y, self.imagen.get_width(), self.imagen.get_height())


class Perro(Enemigo):
    imagen = pygame.transform.scale(pygame.image.load("image/perro.png"), (54, 64))  # Una sola vez, compartida por todos los perros
    velocidad = 0.5

    def __init__(self):
        x, y = posicion_random_borde()
        super().__init__(x, y)


def reponer_perros():
    # Si hay menos perros que "cantidad_perros" (porque algunos fueron
    # eliminados por una pizza), agrega los que falten para completar
    # la cantidad original, apareciendo desde un borde al azar.
    global perros
    faltantes = cantidad_perros - len(perros)
    for _ in range(faltantes):
        perros.append(Perro())


# Armamos la lista de perros con un for, así cada uno es una instancia
# independiente (si usáramos [Perro()] * cantidad_perros, todos apuntarían
# al mismo objeto en memoria y se moverían pegados).
perros = []
for _ in range(cantidad_perros):
    perros.append(Perro())

# Pizza
pizza_img = pygame.image.load("image/pizza.png")  # Cargar la imagen de la pizza
pizza_img = pygame.transform.scale(pizza_img, (32, 32))  # Ajustar el tamaño de la pizza
pizzas = []  # Lista de pizzas en vuelo, cada una es un dict con x, y, dx, dy
velocidad_pizza = 1.6  # Velocidad de movimiento de la pizza
intervalo_lanzamiento = 1000  # Tiempo entre lanzamientos en milisegundos
ultimo_lanzamiento = pygame.time.get_ticks()  # Momento del último lanzamiento
distancia_impacto = 45  # Distancia máxima para considerar que una pizza "le pegó" a un perro

# Vidas del repartidor
vidas = 3  # Vidas iniciales del repartidor

duracion_invulnerabilidad = 1000  # Milisegundos de invulnerabilidad tras perder una vida
invulnerable_hasta = 0  # Timestamp (ms) hasta el cual el repartidor es invulnerable

# Corazones (HUD de vidas)
corazon_img = pygame.image.load("image/corazon.png")  # Cargar la imagen del corazón
corazon_img = pygame.transform.scale(corazon_img, (32, 32))  # Ajustar el tamaño del corazón


def repartidor(x, y):
    # Dibuja al repartidor en la posición (x, y) que le pasemos
    pantalla.blit(repartidor_img, (x, y))


def perro_mas_cercano(origen_x, origen_y, perros):
    # Recibe una posición de origen (por ejemplo, la del repartidor) y la
    # lista completa de perros. Devuelve la posición (x, y) del perro que
    # está más cerca de ese origen, calculando distancia con Pitágoras.
    mas_cercano = None
    menor_distancia = None
    for perro_actual in perros:
        px, py = perro_actual.x, perro_actual.y
        distancia = ((px - origen_x) ** 2 + (py - origen_y) ** 2) ** 0.5
        if menor_distancia is None or distancia < menor_distancia:
            menor_distancia = distancia
            mas_cercano = (px, py)
    return mas_cercano


def detectar_colisiones():
    # Revisa cada pizza contra cada perro. Si una pizza está lo suficientemente
    # cerca de un perro, se considera "impacto": el perro desaparece y la
    # pizza también (no sigue de largo atravesando al perro).
    global pizzas, puntaje

    pizzas_sobrevivientes = []

    for pizza_actual in pizzas:
        pizza_choco = False  # Marca si ESTA pizza ya impactó a algún perro

        for perro_actual in perros[:]:  # [:] = copia, para poder borrar de "perros" sin romper el for
            dx = pizza_actual["x"] - perro_actual.x
            dy = pizza_actual["y"] - perro_actual.y
            distancia = (dx ** 2 + dy ** 2) ** 0.5

            if distancia < distancia_impacto:
                perros.remove(perro_actual)  # Sacamos al perro alcanzado
                sonido_golpe.play()
                pizza_choco = True
                puntaje += 1  # Incrementamos el puntaje por cada perro eliminado
                break  # Esta pizza ya cumplió su función, no sigue comparando

        if not pizza_choco:
            pizzas_sobrevivientes.append(pizza_actual)  # Solo sobreviven las que no pegaron

    pizzas = pizzas_sobrevivientes


def detectar_colision_repartidor(tiempo_actual):
    # Revisa si algún perro tocó al repartidor, usando pygame.Rect en vez
    # de distancia entre puntos: esto compara los rectángulos reales de
    # cada imagen (posición + ancho + alto), no un umbral inventado.
    global vidas, invulnerable_hasta

    # Rect del repartidor: su posición actual + su tamaño real (64x100)
    repartidor_rect = pygame.Rect(repartidor_x, repartidor_y, 64, 100)

    perros_que_tocaron = []
    for perro_actual in perros[:]:  # [:] = copia, para poder borrar de "perros" sin romper el for
        if repartidor_rect.colliderect(perro_actual.rect()):
            perros.remove(perro_actual)
            perros_que_tocaron.append(perro_actual)

    if perros_que_tocaron and tiempo_actual >= invulnerable_hasta:
        vidas -= 1
        sonido_vida_perdida.play()
        invulnerable_hasta = tiempo_actual + duracion_invulnerabilidad

def mostrar_puntaje():
    # Renderiza el puntaje en la pantalla
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))  # Color blanco
    pantalla.blit(texto_puntaje, (650, 10))  # Posición del puntaje en la pantalla


def formatear_tiempo(tiempo_ms):
    # Convierte milisegundos a un string "M:SS"
    minutos = tiempo_ms // 60000
    segundos = (tiempo_ms // 1000) % 60
    return f"{minutos}:{segundos:02d}"


def mostrar_cronometro(tiempo_transcurrido_ms):
    # Renderiza el cronómetro centrado arriba de la pantalla
    texto_tiempo = fuente.render(f"Tiempo: {formatear_tiempo(tiempo_transcurrido_ms)}", True, (255, 255, 255))
    rect_tiempo = texto_tiempo.get_rect(center=(400, 20))
    pantalla.blit(texto_tiempo, rect_tiempo)


def mostrar_pantalla_final(tiempo_transcurrido_ms):
    # Dibuja el cartel de fin de juego: fondo semitransparente + GAME OVER + puntaje + tiempo
    overlay = pygame.Surface((500, 200), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    pantalla.blit(overlay, (150, 200))

    texto_game_over = fuente_grande.render("GAME OVER", True, (0, 0, 0))
    rect_game_over = texto_game_over.get_rect(center=(400, 250))
    pantalla.blit(texto_game_over, rect_game_over)

    texto_puntaje_final = fuente.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
    rect_puntaje_final = texto_puntaje_final.get_rect(center=(400, 310))
    pantalla.blit(texto_puntaje_final, rect_puntaje_final)

    texto_tiempo_final = fuente.render(f"Tiempo sobrevivido: {formatear_tiempo(tiempo_transcurrido_ms)}", True, (0, 0, 0))
    rect_tiempo_final = texto_tiempo_final.get_rect(center=(400, 350))
    pantalla.blit(texto_tiempo_final, rect_tiempo_final)


# Bucle principal del juego
se_ejecuta = True  # Variable para controlar el bucle principal
while se_ejecuta:
    # --- Detección de eventos (teclado, cerrar ventana, etc.) ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                repartidor_x_cambio = -velocidad_repartidor
            if evento.key == pygame.K_RIGHT:
                repartidor_x_cambio = velocidad_repartidor
            if evento.key == pygame.K_UP:
                repartidor_y_cambio = -velocidad_repartidor
            if evento.key == pygame.K_DOWN:
                repartidor_y_cambio = velocidad_repartidor
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                repartidor_x_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                repartidor_y_cambio = 0

    tiempo_actual = pygame.time.get_ticks()

    if estado_juego == "jugando":
        # --- Movimiento del repartidor según las teclas apretadas ---
        repartidor_x += repartidor_x_cambio
        repartidor_y += repartidor_y_cambio

        # Límites de pantalla para que el repartidor no se salga
        if repartidor_x < 0:
            repartidor_x = 0
        if repartidor_x > 800 - 64:
            repartidor_x = 800 - 64
        if repartidor_y < 0:
            repartidor_y = 0
        if repartidor_y > 600 - 100:
            repartidor_y = 600 - 100

        # --- Movimiento de cada perro: todos persiguen al repartidor ---
        for perro_actual in perros:
            perro_actual.mover_hacia(repartidor_x, repartidor_y)

        # --- Separación entre perros para que no se superpongan ---
        distancia_minima = 60  # Distancia mínima deseada entre perros (ajustable)
        for perro_actual in perros:
            for otro_perro in perros:
                if perro_actual is otro_perro:
                    continue  # No comparar un perro consigo mismo
                dx = perro_actual.x - otro_perro.x
                dy = perro_actual.y - otro_perro.y
                distancia = (dx ** 2 + dy ** 2) ** 0.5
                if 0 < distancia < distancia_minima:
                    empuje_x = (dx / distancia) * (distancia_minima - distancia) * 0.1
                    empuje_y = (dy / distancia) * (distancia_minima - distancia) * 0.1
                    perro_actual.x += empuje_x
                    perro_actual.y += empuje_y

        # --- Lanzamiento automático de pizzas cada 1 segundo ---
        if tiempo_actual - ultimo_lanzamiento >= intervalo_lanzamiento:
            ultimo_lanzamiento = tiempo_actual
            objetivo = perro_mas_cercano(repartidor_x, repartidor_y, perros)
            if objetivo is not None:
                objetivo_x, objetivo_y = objetivo
                odx = objetivo_x - repartidor_x
                ody = objetivo_y - repartidor_y
                odistancia = (odx ** 2 + ody ** 2) ** 0.5
                if odistancia != 0:
                    pdx = (odx / odistancia) * velocidad_pizza
                    pdy = (ody / odistancia) * velocidad_pizza
                else:
                    pdx, pdy = 0, velocidad_pizza
                pizzas.append({"x": repartidor_x, "y": repartidor_y, "dx": pdx, "dy": pdy})
                sonido_disparo.play()

        # --- Actualizar posición de las pizzas y descartar las que salieron ---
        pizzas_en_pantalla = []
        for pizza in pizzas:
            pizza["x"] += pizza["dx"]
            pizza["y"] += pizza["dy"]
            if 0 <= pizza["x"] <= 800 and 0 <= pizza["y"] <= 600:
                pizzas_en_pantalla.append(pizza)
        pizzas = pizzas_en_pantalla

        reponer_perros()

    # --- Colisiones: pizza que toca a un perro lo elimina ---
    detectar_colisiones()
    detectar_colision_repartidor(tiempo_actual)

    # --- Fin del juego: se detecta una sola vez, al quedarse sin vidas ---
    if estado_juego == "jugando" and vidas <= 0:
        estado_juego = "terminado"
        tiempo_final = tiempo_actual - tiempo_inicio
        pygame.mixer.music.stop()

    # --- Dibujado de todo el frame ---
    pantalla.blit(fondo, (0, 0))

    invulnerable = tiempo_actual < invulnerable_hasta
    if not invulnerable or (tiempo_actual // 100) % 2 == 0:
        repartidor(repartidor_x, repartidor_y)

    for perro_actual in perros:
        perro_actual.dibujar()
    for pizza in pizzas:
        pantalla.blit(pizza_img, (pizza["x"], pizza["y"]))

    for i in range(vidas):
        pantalla.blit(corazon_img, (10 + i * 36, 10))

    mostrar_puntaje()

    if estado_juego == "jugando":
        mostrar_cronometro(tiempo_actual - tiempo_inicio)
    else:
        mostrar_cronometro(tiempo_final)
        mostrar_pantalla_final(tiempo_final)

    pygame.display.update()

pygame.quit()