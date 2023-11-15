import pygame
from configuraciones import *
from plataforma import *
from personaje import *
from utilidades import *
class Enemigo_estatico:
    def __init__(self,eje_x,eje_y,ancho,alto,path_imagen) -> None:
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = eje_x
        self.rect.y = eje_y
        self.lados = obtener_rectangulos(self.rect)
        self.se_blitea = True


    def update(self, pantalla,lista_plataformas):
        if self.se_blitea:
            pantalla.blit(self.imagen,self.rect)
        

            if get_mode():
                for lado in self.lados:
                    pygame.draw.rect(pantalla,(0,0,255),self.lados[lado],2)
        

        
    
        




        

