import pygame
from configuraciones import *

class Meta:
    def __init__(self,eje_x,eje_y,ancho,alto,path_imagen) -> None:
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = eje_x
        self.rect.y = eje_y

    def update(self, pantalla):
        pantalla.blit(self.imagen,self.rect)