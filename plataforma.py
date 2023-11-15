import pygame
from configuraciones import *
from modo import *
from utilidades import *

class Plataforma:
    def __init__(self,eje_x,eje_y, ancho , alto , path_imagen = None) -> None:
        if path_imagen != None:
            self.imagen = pygame.image.load(path_imagen)
            self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
            self.rect = self.imagen.get_rect()
        else:
            self.imagen = None
            self.rect = pygame.Rect(eje_x,eje_y,ancho,alto)
        self.rect.x = eje_x
        self.rect.y = eje_y
        self.lados = obtener_rectangulos(self.rect)

    def update(self, pantalla):
        if self.imagen != None:
            pantalla.blit(self.imagen,self.rect)
        if get_mode():
            for lado in self.lados:
                pygame.draw.rect(pantalla,(0,0,255),self.lados[lado],2)
            

    