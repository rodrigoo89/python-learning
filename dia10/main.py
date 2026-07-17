import pygame
from perro import Perro
from gato import Gato
from pizza import Pizza
from repartidor import Repartidor
from interfaz import Interfaz
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
repartidor = Repartidor(368, 460)  # Posición inicial

# Perro
cantidad_perros = 2  # Cambiás este número para ajustar la cantidad de perros en juego
cantidad_gatos = 2  # Cambiás este número para ajustar la cantidad de gatos en juego
# Puntaje
puntaje = 0  # Inicializamos el puntaje en cero
interfaz = Interfaz()
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





tipos_enemigos = [(Perro, cantidad_perros), (Gato, cantidad_gatos)]  # Clase + cantidad deseada de cada una


def reponer_enemigos():
    # Si hay menos enemigos de algún tipo que su cantidad deseada (porque
    # algunos fueron eliminados por una pizza), agrega los que falten para
    # completar la cantidad original, apareciendo desde un borde al azar.
    global enemigos
    for clase, cantidad_deseada in tipos_enemigos:
        cantidad_actual = sum(1 for enemigo in enemigos if isinstance(enemigo, clase))
        faltantes = cantidad_deseada - cantidad_actual
        for _ in range(faltantes):
            enemigos.append(clase())


# Armamos la lista de enemigos con un for, así cada uno es una instancia
# independiente (si usáramos [Perro()] * cantidad_perros, todos apuntarían
# al mismo objeto en memoria y se moverían pegados).
enemigos = []
for clase, cantidad in tipos_enemigos:
    for _ in range(cantidad):
        enemigos.append(clase())


# Pizza
pizzas = []  # Lista de pizzas en vuelo (instancias de Pizza)
intervalo_lanzamiento = 1000  # Tiempo entre lanzamientos en milisegundos
ultimo_lanzamiento = pygame.time.get_ticks()  # Momento del último lanzamiento
distancia_impacto = 45  # Distancia máxima para considerar que una pizza "le pegó" a un perro


def enemigo_mas_cercano(origen_x, origen_y, enemigos):
    # Recibe una posición de origen (por ejemplo, la del repartidor) y la
    # lista completa de enemigos (perros, gatos, etc.). Devuelve la posición
    # (x, y) del enemigo que está más cerca de ese origen, con Pitágoras.
    mas_cercano = None
    menor_distancia = None
    for enemigo_actual in enemigos:
        ex, ey = enemigo_actual.x, enemigo_actual.y
        distancia = ((ex - origen_x) ** 2 + (ey - origen_y) ** 2) ** 0.5
        if menor_distancia is None or distancia < menor_distancia:
            menor_distancia = distancia
            mas_cercano = (ex, ey)
    return mas_cercano


def detectar_colisiones():
    # Revisa cada pizza contra cada enemigo. Si una pizza está lo suficientemente
    # cerca de un enemigo, se considera "impacto": el enemigo desaparece y la
    # pizza también (no sigue de largo atravesándolo).
    global pizzas, puntaje

    pizzas_sobrevivientes = []

    for pizza_actual in pizzas:
        pizza_choco = False  # Marca si ESTA pizza ya impactó a algún enemigo

        for enemigo_actual in enemigos[:]:  # [:] = copia, para poder borrar de "enemigos" sin romper el for
            dx = pizza_actual.x - enemigo_actual.x
            dy = pizza_actual.y - enemigo_actual.y
            distancia = (dx ** 2 + dy ** 2) ** 0.5

            if distancia < distancia_impacto:
                enemigos.remove(enemigo_actual)  # Sacamos al enemigo alcanzado
                sonido_golpe.play()
                pizza_choco = True
                puntaje += 1  # Incrementamos el puntaje por cada enemigo eliminado
                break  # Esta pizza ya cumplió su función, no sigue comparando

        if not pizza_choco:
            pizzas_sobrevivientes.append(pizza_actual)  # Solo sobreviven las que no pegaron

    pizzas = pizzas_sobrevivientes


def detectar_colision_repartidor(tiempo_actual):
    # Revisa si algún enemigo tocó al repartidor, usando pygame.Rect en vez
    # de distancia entre puntos: esto compara los rectángulos reales de
    # cada imagen (posición + ancho + alto), no un umbral inventado.
    enemigos_que_tocaron = []
    for enemigo_actual in enemigos[:]:  # [:] = copia, para poder borrar de "enemigos" sin romper el for
        if repartidor.rect().colliderect(enemigo_actual.rect()):
            enemigos.remove(enemigo_actual)
            enemigos_que_tocaron.append(enemigo_actual)

    if enemigos_que_tocaron and tiempo_actual >= repartidor.invulnerable_hasta:
        repartidor.perder_vida(tiempo_actual)
        sonido_vida_perdida.play()

# Bucle principal del juego
se_ejecuta = True  # Variable para controlar el bucle principal
while se_ejecuta:
    # --- Detección de eventos (teclado, cerrar ventana, etc.) ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                repartidor.x_cambio = -repartidor.velocidad
            if evento.key == pygame.K_RIGHT:
                repartidor.x_cambio = repartidor.velocidad
            if evento.key == pygame.K_UP:
                repartidor.y_cambio = -repartidor.velocidad
            if evento.key == pygame.K_DOWN:
                repartidor.y_cambio = repartidor.velocidad
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                repartidor.x_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                repartidor.y_cambio = 0

    tiempo_actual = pygame.time.get_ticks()

    if estado_juego == "jugando":
        # --- Movimiento del repartidor según las teclas apretadas ---
        repartidor.mover()

        # --- Movimiento de cada enemigo: todos persiguen al repartidor ---
        for enemigo_actual in enemigos:
            enemigo_actual.mover_hacia(repartidor.x, repartidor.y)

        # --- Separación entre enemigos para que no se superpongan ---
        distancia_minima = 60  # Distancia mínima deseada entre enemigos (ajustable)
        for enemigo_actual in enemigos:
            for otro_enemigo in enemigos:
                if enemigo_actual is otro_enemigo:
                    continue  # No comparar un enemigo consigo mismo
                dx = enemigo_actual.x - otro_enemigo.x
                dy = enemigo_actual.y - otro_enemigo.y
                distancia = (dx ** 2 + dy ** 2) ** 0.5
                if 0 < distancia < distancia_minima:
                    empuje_x = (dx / distancia) * (distancia_minima - distancia) * 0.1
                    empuje_y = (dy / distancia) * (distancia_minima - distancia) * 0.1
                    enemigo_actual.x += empuje_x
                    enemigo_actual.y += empuje_y

        # --- Lanzamiento automático de pizzas cada 1 segundo ---
        if tiempo_actual - ultimo_lanzamiento >= intervalo_lanzamiento:
            ultimo_lanzamiento = tiempo_actual
            objetivo = enemigo_mas_cercano(repartidor.x, repartidor.y, enemigos)
            if objetivo is not None:
                objetivo_x, objetivo_y = objetivo
                pizzas.append(Pizza(repartidor.x, repartidor.y, objetivo_x, objetivo_y))
                sonido_disparo.play()

        # --- Actualizar posición de las pizzas y descartar las que salieron ---
        pizzas_en_pantalla = []
        for pizza in pizzas:
            pizza.mover()
            if pizza.dentro_de_pantalla():
                pizzas_en_pantalla.append(pizza)
        pizzas = pizzas_en_pantalla

        reponer_enemigos()

    # --- Colisiones: pizza que toca a un enemigo lo elimina ---
    detectar_colisiones()
    detectar_colision_repartidor(tiempo_actual)

    # --- Fin del juego: se detecta una sola vez, al quedarse sin vidas ---
    if estado_juego == "jugando" and repartidor.vidas <= 0:
        estado_juego = "terminado"
        tiempo_final = tiempo_actual - tiempo_inicio
        pygame.mixer.music.stop()

    # --- Dibujado de todo el frame ---
    pantalla.blit(fondo, (0, 0))

    repartidor.dibujar(pantalla, tiempo_actual)

    for enemigo_actual in enemigos:
        enemigo_actual.dibujar(pantalla)
    for pizza in pizzas:
        pizza.dibujar(pantalla)

    interfaz.mostrar_vidas(pantalla, repartidor.vidas)
    interfaz.mostrar_puntaje(pantalla, puntaje)

    if estado_juego == "jugando":
        interfaz.mostrar_cronometro(pantalla, tiempo_actual - tiempo_inicio)
    else:
        interfaz.mostrar_cronometro(pantalla, tiempo_final)
        interfaz.mostrar_pantalla_final(pantalla, puntaje, tiempo_final)

    pygame.display.update()

pygame.quit()