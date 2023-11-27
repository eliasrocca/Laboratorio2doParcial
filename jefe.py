import pygame
from configuraciones import *
from plataforma import *
from personaje import *
from utilidades import *
from modo import *
from disparo import *

class Jefe:
    def __init__(self,eje_x,eje_y,ancho,alto,path_imagen) -> None:
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        reescalar_imagenes_boss(ancho,alto)
        self.rect = self.imagen.get_rect()
        self.rect.x = eje_x
        self.rect.y = eje_y
        self.lados = obtener_rectangulos(self.rect)
        self.orientacion = "derecha"
        self.velocidad = 5
        self.se_blitea = True
        self.esta_en_pantalla = True
        self.contador_pasos = 0
        self.animacion = boss_quieto_der
        self.vidas = 10
        self.flag_disparo = True
        self.tiempo_ultimo_disparo = 0
        self.lista_proyectiles = []
        self.puntos = 10
        

    def update(self, pantalla,lista_plataformas,personaje,lista_vidas):
        if self.se_blitea:
            
        
            self.mover(pantalla)
            self.verificar_limites(lista_plataformas)
            self.verificar_muerte()
            self.animar(pantalla)
            self.actualizar_proyectiles(pantalla,personaje,lista_vidas)   
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

    def lanzar_proyectil(self):
        x = None
        margen = 47

        y = self.rect.centery + 10
        if self.orientacion == "derecha":
            x = self.rect.right - margen
        elif self.orientacion == "izquierda":
            x = self.rect.left - 100 + margen

        if x is not None:
            self.lista_proyectiles.append(Disparo(x,y,self.orientacion))

    def actualizar_proyectiles(self,pantalla,personaje,lista_vidas):
        i = 0
        while i < len(self.lista_proyectiles):
            p= self.lista_proyectiles[i]
            p.update(pantalla,personaje,lista_vidas)
            if p.se_blitea == False:
                self.lista_proyectiles.pop(i)
                i -= 1
            i += 1

    def mover(self,pantalla):
        if self.orientacion == "derecha":
            self.animacion = boss_camina_der
            movimiento = self.velocidad
        elif self.orientacion == "izquierda":
            self.animacion = boss_camina_izq
            movimiento = self.velocidad * -1
        
        for lado in self.lados:
            self.lados[lado].x += movimiento

        if self.flag_disparo:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_disparo >= 3000:
                self.tiempo_ultimo_disparo = tiempo_actual
                self.lanzar_proyectil()
                # self.flag_disparo = False




    def animar(self,pantalla):
        largo = len(self.animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion[self.contador_pasos],self.rect)
        self.contador_pasos += 1
        
    def recibir_daño(self):
        self.vidas -= 1
        print(self.vidas)

    def verificar_muerte(self):
        if self.vidas == 0:
            self.se_blitea = False