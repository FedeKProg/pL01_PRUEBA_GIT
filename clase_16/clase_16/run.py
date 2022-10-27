import pygame
from constantes import *
import tablero

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA+100))
pygame.display.set_caption('The Simpsons Memotest')

running = True
#cuadrado = pygame.Rect(30, 30, 60, 60)
#set tick timer 
tick = pygame.USEREVENT
pygame.time.set_timer(tick,1000)

tablero_juego = tablero.init()
while running:

    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            tablero.colicion(tablero_juego,event.pos)
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                print("Ya paso un segundo")
        
    # Se pinta el fondo de la ventana de blanco
    pantalla_juego.fill((255, 255, 255))
    # Se dibuja un circulo azul
   # pygame.draw.circle(pantalla_juego, (0, 0, 255), (250, 250), 75)
    # Se dibuja un cuadrado amarillo
    #pygame.draw.rect(pantalla_juego, (255, 255, 0), cuadrado)
    #imagen = pygame.image.load(r"C:\Users\Profesor\Desktop\PL1_PY_2022_2C\clase_16\recursos\01.png")
    #pygame.transform.scale(imagen, (100,100))
   # pantalla_juego.blit(imagen,(50,50))
   # font = pygame.font.SysFont("Arial Narrow", 50)
    #text = font.render("HOLA MUNDO", True, (255, 0, 0))
    #pantalla_juego.blit(text,(100,100))
    # Muestra los cambios en  la pantalla

    tablero.render(tablero_juego,pantalla_juego)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()