import pygame
from configuraciones import *
from plataforma import *
from personaje import *
from utilidades import *
class Enemigo:
    def __init__(self,eje_x,eje_y,ancho,alto,path_imagen) -> None:
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = eje_x
        self.rect.y = eje_y
        self.lados = obtener_rectangulos(self.rect)
        self.orientacion = "derecha"
        self.velocidad = 5
        self.se_blitea = True
        self.esta_en_pantalla = True

    def update(self, pantalla,lista_plataformas):
        if self.se_blitea:
            pantalla.blit(self.imagen,self.rect)
        
            self.mover()
            self.verificar_limites(lista_plataformas)
            if get_mode():
                for lado in self.lados:
                    pygame.draw.rect(pantalla,(0,0,255),self.lados[lado],2)
        
        elif self.esta_en_pantalla:
            pantalla.blit(self.imagen,self.rect)
            for lado in self.lados:
                self.lados[lado].y += 5
            if self.rect.top > pantalla.get_height():
                self.esta_en_pantalla = False
        
    
        

    def verificar_limites(self,lista_plataformas):
        izquierda_en_aire = True
        derecha_en_aire = True
        for plataforma in lista_plataformas:
            if self.lados['left'].colliderect(plataforma.lados['top']):
                izquierda_en_aire = False
                
            if self.lados['right'].colliderect(plataforma.lados['top']):
                derecha_en_aire = False
        
        if izquierda_en_aire:
            self.orientacion = "derecha"
        elif derecha_en_aire:
            self.orientacion = "izquierda"


    def mover(self):
        if self.orientacion == "derecha":
            movimiento = self.velocidad
        elif self.orientacion == "izquierda":
            movimiento = self.velocidad * -1
        
        for lado in self.lados:
            self.lados[lado].x += movimiento
        

