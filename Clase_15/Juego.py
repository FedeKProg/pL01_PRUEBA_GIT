import elementos
import pygame
import colores
import personaje

pygame.init()


Ancho_ventana = 800
Alto_ventana = 800

main_screen = pygame.display.set_mode((Ancho_ventana, Alto_ventana))
pygame.display.set_caption("Bienvenido al juego de Fede")
main_screen.fill((colores.NEGRO))
pygame.display.flip()

timer_juego = pygame.USEREVENT
pygame.time.set_timer(timer_juego, 500)


lista_donas = []
for i in range(10):
    lista_donas.append(elementos.setear_dona(0+i*50,0,200,200))

# lista_donas = elementos.crear_lista(10)
player = personaje.crear_personaje(Ancho_ventana/2, Alto_ventana-200,200,200)

running = True

while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.USEREVENT:
            if event.type == timer_juego:
                elementos.update(lista_donas)
        lista_teclas = pygame.key.get_pressed()
        if lista_teclas [pygame.K_RIGHT]:
            personaje.movimiento_personaje(player, 10)
        elif lista_teclas [pygame.K_LEFT]:
            personaje.movimiento_personaje(player, -10)

    personaje.screen_update(player, main_screen)
    elementos.screen_update(lista_donas, player, main_screen)

    pygame.display.flip()
pygame.quit()