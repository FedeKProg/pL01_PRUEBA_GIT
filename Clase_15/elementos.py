import pygame
import colores

def setear_dona(x,y,ancho,alto):
	imagen_dona = pygame.image.load("dona.png.png")
	imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
	rect_dona = imagen_dona.get_rect()
	rect_dona.x = x
	rect_dona.y = y
	dict_dona = {}
	dict_dona["surface"] = imagen_dona
	dict_dona["rect"] = rect_dona
	return dict_dona

def screen_update(lista_donas, personaje, main_screen):
	for dona in lista_donas:
		if dona["visible"] and personaje["rect"].colliderect(dona["rect"]):
			dona["visible"] = False
			personaje["score"] = personaje["score"] + 100
		if dona["visible"]:
			pygame.draw.rect(main_screen, colores.VERDE,dona["rect"])
			main_screen.blit(dona["surface"], dona["rect"])
	font = pygame.font.SysFont("Times New Roman", 50)
	text = font.render("SCORE: {0}".format(personaje["score"]), True, (255,0,0))
	main_screen.blit(text,(0,0))

		# pygame.draw.rect(main_screen, (0, 0, 255), (100, 100,200,200))
		# main_screen.blit(dona["surface"], dona["rect"])

def crear_lista(cantidad):
	lista_donas = []
	for i in range(cantidad):
		lista_donas.append(setear_dona(0+i*50,0,200,200))
	return

def update(lista_donas):
	for dona in lista_donas:
		rect_dona = dona["rect"]
		rect_dona.y = rect_dona.y + 100
