import pygame
import math
import random
import tarjeta
from constantes import *

class Tablero:
	def __init__(self) -> None:
		lista_tarjetas = []
		i = 1
		for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
			for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
				if(i > CANTIDAD_TARJETAS_UNICAS):
					tarjeta_test = tarjeta.init("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"00.png",x,y)
				else:
					tarjeta_test = tarjeta.init("0{0}.png".format(i),r"00.png",x,y)
				lista_tarjetas.append(tarjeta_test)
				i = i + 1
		self.l_tarjetas = lista_tarjetas
		self.tiempo_ultimo_destape = 0


	# def init():
	# 	'''
	# 	Crea una lista de tarjetas
	# 	Recibe como parametro la cantidad de tarjetas
	# 	Retorna un dict tablero
	# 	'''
		
	# 	d_tablero = {}
	# 	lista_tarjetas = []
	# 	i = 1
	# 	for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
	# 		for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
	# 			if(i > CANTIDAD_TARJETAS_UNICAS):
	# 				tarjeta_test = tarjeta.init("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"00.png",x,y)
	# 			else:
	# 				tarjeta_test = tarjeta.init("0{0}.png".format(i),r"00.png",x,y)
	# 			lista_tarjetas.append(tarjeta_test)
	# 			i = i + 1
	# 	d_tablero["l_tarjetas"] = lista_tarjetas
	# 	d_tablero["tiempo_ultimo_destape"] = 0
	# 	return d_tablero

	def colicion(self,pos_xy):
		'''
		verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
		Recibe como parametro el tablero y una tupla (X,Y)
		Retorna el indice de la tarjeta que colisiono con la coordenada
		'''
		lista_tarjetas = self.l_tarjetas
		if(tarjeta.cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas) < 2):
			for aux_tarjeta in lista_tarjetas:
				if(aux_tarjeta["rect"].collidepoint(pos_xy)):
					aux_tarjeta["visible"]=True
					self.tiempo_ultimo_destape = pygame.time.get_ticks()

	def update(self):
		'''
		verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
		Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
		'''
		tiempo_actual = pygame.time.get_ticks()
		if(tiempo_actual - self.tiempo_ultimo_destape > 3000 and self.tiempo_ultimo_destape > 0):
		self.tiempo_ultimo_destape = 0
		lista_tarjetas = self.l_tarjetas
		for aux_tarjeta in lista_tarjetas:
			if(aux_tarjeta["descubierto"]==False):
				aux_tarjeta["visible"]=False
		
		if(d_tablero["tiempo_ultimo_destape"] > 0):
			if(tarjeta.match(d_tablero["l_tarjetas"])):
				d_tablero["tiempo_ultimo_destape"] = 0


	def render(d_tablero,pantalla_juego):
		'''
		Dibuja todos los elementos del tablero en la superficie recibida como parametro
		Recibe como parametro el tablero
		'''
		lista_tarjetas = self.l_tarjetas
		for tarjeta in lista_tarjetas:
			if(tarjeta["visible"]):
				pantalla_juego.blit(tarjeta["surface"],tarjeta["rect"])
			else:
				pantalla_juego.blit(tarjeta["surface_hide"],tarjeta["rect"])
	 