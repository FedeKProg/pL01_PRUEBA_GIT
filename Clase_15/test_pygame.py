from cmath import rect
import pygame
import elementos

pygame.init()

# running = True

# window = pygame.display.set_mode((500, 400), 0, 32)
# pygame.display.set_caption("Vamos hacer un juego!")
# while(running):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     window.fill((255, 255, 255))
#     pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
#     pygame.display.flip()
# pygame.quit

Ancho_ventana = 800
Alto_ventana = 800

#setear tamaño pantalla
main_screen = pygame.display.set_mode((Ancho_ventana, Alto_ventana))
#setear nombre de la ventana
pygame.display.set_caption("Bienvenido al juego de Fede")
#setear color de fondo
main_screen.fill((26,45,29))
#funcion para actualizar la pantalla con el ultimo codigo
pygame.display.flip()

running = True
pos_circ = [500, 350]

#crear timer
timer_juego = pygame.USEREVENT
pygame.time.set_timer(timer_juego, 500)

#añadir texto

font = pygame.font.SysFont("Times New Roman", 20)
text = font.render("Que rico rosquillas", True, (255,255,255))

#añadir imagen
lista_homeros = []
for i in range(10):
    lista_homeros.append(elementos.setear_dona(0+i*50,0,200,200))

while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False 
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #    print(event.pos)
        #    pos_circ = list(event.pos)
        # if event.type == pygame.USEREVENT:    
        #     if event.type == timer_juego:
        #         if pos_circ[0] < Ancho_ventana + 65:
        #             pos_circ[0] = pos_circ[0] + 10
        #         else: 
        #             pos_circ[0] = -75
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         pos_circ[1] = pos_circ[1] + 10
        #     elif event.key == pygame.K_LEFT:
        #         pos_circ[1] = pos_circ[1] - 10

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas [pygame.K_RIGHT]:
        pos_circ[1] = pos_circ[1] + 1
    elif lista_teclas [pygame.K_LEFT]:
            pos_circ[1] = pos_circ[1] - 1


    main_screen.fill((50, 130, 102))
    pygame.draw.circle(main_screen, (255, 0, 0), pos_circ, 75)
    pygame.draw.rect(main_screen, (0, 0, 255), (200, 200, 500, 350),75)
                                    #color      #posicion - tamaño
    # main_screen.blit(imagen_homero, (1, 1))
    
    # pygame.draw.rect(main_screen, (0, 0, 255), (100, 100,200,200))
    # main_screen.blit(image, lista_homeros["rect"])

    main_screen.blit(text,(250,250))

    pygame.display.flip()
pygame.quit()