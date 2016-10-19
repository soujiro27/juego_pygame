import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
color=pygame.Color(0,0,0)
colorLinea=pygame.Color(255,0,0)
ventana=pygame.display.set_mode((800,600))
pygame.display.set_caption("juego en pygame")

imagen=pygame.image.load('mario.png')
posx=10
posy=300
velocidad=10	
fondo=pygame.Color(0,0,0)
derecha=True
angulo=0
rectangulo=pygame.Rect(400,300,30,30)
rectangulo_dos=pygame.Rect(200,300,50,50)
while True:
	ventana.fill(fondo)
	#ventana.blit(imagen,(posx,posy))
	pygame.draw.rect(ventana,colorLinea,rectangulo)
	pygame.draw.rect(ventana,(0,255,0),rectangulo_dos)
	if rectangulo.colliderect(rectangulo_dos):
		velocidad=0
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()
		if evento.type==pygame.KEYUP:
			if evento.key==K_LEFT:
				rectangulo.left=rectangulo.left-velocidad
			if evento.key==K_RIGHT:	
				rectangulo.right=rectangulo.right+velocidad
			if evento.key==K_UP:
				posy=posy-velocidad
		
				imagen=pygame.transform.rotate(imagen,90)
					
			if evento.key==K_DOWN:
				posy=posy+velocidad
				
				imagen=pygame.transform.rotate(imagen,-90)
	#posx,posy= pygame.mouse.get_pos()

	rectangulo_dos.left, rectangulo_dos.top=pygame.mouse.get_pos()
	pygame.display.update()


















