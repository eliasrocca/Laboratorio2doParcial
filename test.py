import pygame
import sys
from pygame.locals import *
from GUI_form_prueba import FormPrueba

pygame.init()
WIDTH = 1400
HEIGHT = 700
FPS = 60

reloj = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((WIDTH, HEIGHT))

form_prueba = FormPrueba(PANTALLA)
while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    form_prueba.update(eventos)
    
    
    
    pygame.display.flip()