import pygame
import math
import random
from constantes import *

class Trajeta:

    def __init__(self,nombre_imagen,nombre_imagen_hide,x,y):
        '''
        Crea una nueva tarjeta
        Recibe como parametro el path donde estan los recursos, el nombre de la imagen y el tamaño que esta debera tener
        Retorna la tarjeta creada
        '''
        nueva_tarjeta = {}
        nueva_tarjeta["visible"]=False
        nueva_tarjeta["descubierto"]=False
        nueva_tarjeta["path_imagen"] = PATH_RECURSOS+nombre_imagen
        nueva_tarjeta["surface"] = pygame.transform.scale(pygame.image.load(nueva_tarjeta["path_imagen"]), (ANCHO_TARJETA,ALTO_TARJETA))
        nueva_tarjeta["surface_hide"] = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA,ALTO_TARJETA))
        nueva_tarjeta["rect"] = nueva_tarjeta["surface"].get_rect()
        nueva_tarjeta["rect"].x = x
        nueva_tarjeta["rect"].y = y
        return nueva_tarjeta

    def cantidad_tarjetas_descubiertas(lista_tarjetas):
        cantidad = 0
        for tarjeta in lista_tarjetas:
            if(tarjeta["descubierto"]):
                cantidad += 1
        return cantidad
        

    def cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas):
        cantidad = 0
        for tarjeta in lista_tarjetas:
            if(tarjeta["visible"] and not tarjeta["descubierto"]):
                cantidad += 1
        return cantidad
        
    def match(lista_tarjetas):
        for index_p in range(len(lista_tarjetas)):
            if(lista_tarjetas[index_p]["visible"] and not lista_tarjetas[index_p]["descubierto"]):
                aux_primer_tarjeta = lista_tarjetas[index_p]
                for index_s in range(index_p+1,len(lista_tarjetas)):
                    if(lista_tarjetas[index_s]["visible"] and not lista_tarjetas[index_s]["descubierto"] ):
                        aux_segunda_tarjeta = lista_tarjetas[index_s]
                        if(aux_primer_tarjeta["path_imagen"] == aux_segunda_tarjeta["path_imagen"]):
                            aux_primer_tarjeta["descubierto"]=True
                            aux_segunda_tarjeta["descubierto"]=True
                            return True
        return False
