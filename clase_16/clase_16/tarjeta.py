import pygame
import math
import random
from constantes import *

def init(nombre_imagen,nombre_imagen_hide,x,y):
    '''
    Crea una nueva tarjeta
    Recibe como parametro el path donde estan los recursos, el nombre de la imagen y el tamaño que esta debera tener
    Retorna la tarjeta creada
    '''
    nueva_tarjeta = {}
    nueva_tarjeta["visible"]=True
    nueva_tarjeta["descubierto"]=False
    nueva_tarjeta["path_imagen"] = PATH_RECURSOS+nombre_imagen
    nueva_tarjeta["surface"] = pygame.transform.scale(pygame.image.load(nueva_tarjeta["path_imagen"]), (ANCHO_TARJETA,ALTO_TARJETA))
    nueva_tarjeta["surface_hide"] = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA,ALTO_TARJETA))
    nueva_tarjeta["rect"] = nueva_tarjeta["surface"].get_rect()
    nueva_tarjeta["rect"].x = x
    nueva_tarjeta["rect"].y = y
    return nueva_tarjeta