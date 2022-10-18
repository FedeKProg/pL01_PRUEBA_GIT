from symbol import dictorsetmaker
import elementos
import pygame
import colores

def crear_personaje(x,y,ancho,alto):
    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load("homero_defi.png")
    dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"],(ancho,alto))
    dict_personaje["rect_pos"] = pygame.Rect(x,y,200,200)
    dict_personaje["rect"] = pygame.Rect((x+ancho/2)-10,y+90,50,20)

    # dict_personaje["rect"] = dict_personaje["surface"].get_rect()
    # dict_personaje["rect"].centerx = 400 
    # dict_personaje["rect"].y = 600 
    return dict_personaje

def screen_update(personaje, main_screen):
    pygame.draw.rect(main_screen,colores.ROJO,personaje["rect"])
    main_screen.blit(personaje["surface"],personaje["rect"])

def movimiento_personaje (personaje, incremento_x):
    personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
    personaje["rect"].x = personaje["rect"].x + incremento_x