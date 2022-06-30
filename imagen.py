import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((800,700))
pygame.display.set_caption("Carga imagen y posición al azar")
colorFondo = (1,150,70)
colorRectangulo = (255, 60, 40)

#Carga imagen
imagen = pygame.image.load("imagenes/pygame.png")
#Posición de la imagen
posXIma, posYIma =(120,75)

while True:
    ventana.fill(colorFondo)
    ventana.blit(imagen,(posXIma,posYIma))
    for i in range(15):
        posX, posY = randint(1,700), randint(1,600)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        colorRectangulo = (r, g, b)
        pygame.draw.rect(ventana, colorRectangulo,(posX, posY, 50,50))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

