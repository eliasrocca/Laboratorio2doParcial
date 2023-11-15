import pygame
from configuraciones import *
from modo import *
from utilidades import *
from objetos_recolectables import *
from enemigos import *


class Mario:
    def __init__(self,eje_x,eje_y) -> None:
        self.velocidad = 7
        self.salto = 0
        self.velocidad_salto = 20
        self.estado = "quieto"
        self.esta_saltando = False
        self.esta_cayendo = True
        self.en_tierra = True
        self.orientacion = "derecha" 
        self.contador_pasos = 0
        self.toco_lado_der = False
        self.toco_lado_izq = False
        self.toco_abajo = False
        self.vidas = 3
        self.mario_muere = False
        

        
        reescalar_imagenes_mario(55,70)
        self.imagen = personaje_quieto_der
        self.rect = self.imagen[0].get_rect()
        self.rect.x = eje_x
        self.rect.y = eje_y
        self.lados = obtener_rectangulos(self.rect)

    def update(self,lista_teclas,pantalla, lista_plataformas,lista_consumibles,lista_enemigos,lista_vidas,lista_enemigos_2):
        
        self.verificar_colisiones(lista_plataformas,lista_consumibles,lista_enemigos,lista_vidas,lista_enemigos_2)
        self.movimiento(lista_teclas,pantalla)
        self.gravedad(lista_plataformas)
        if get_mode():
            for lado in self.lados:
                pygame.draw.rect(pantalla,(0,0,255),self.lados[lado],2)
        self.lados = obtener_rectangulos(self.rect)

    def animar(self,lista_imagenes,pantalla):
        largo = len(lista_imagenes)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(lista_imagenes[self.contador_pasos],self.rect)
        self.contador_pasos += 1

    def corregir_desface_lados(self):

            self.lados["top"].topleft = self.rect.topleft 
            self.lados["left"].bottomleft = self.rect.bottomleft
            self.lados["right"].bottomright = self.rect.bottomright
            self.lados["bottom"].bottomleft = self.rect.bottomleft

    def gravedad(self, lista_plataformas):
        if(self.esta_saltando):
            
            self.salto += 7
            self.rect.y -= 7
            # print("Esta saltando")
            if self.salto >= 130 or self.toco_abajo:
                self.esta_saltando = False
                self.esta_cayendo = True
                self.salto = 0
                self.estado = "quieto"
                # print("Dejo de saltar")
        else:
            self.esta_cayendo = True
            for plataforma in lista_plataformas:
                if self.lados['bottom'].colliderect(plataforma.lados['top']):
                    self.salto = 0
                    self.rect.bottom = plataforma.rect.top + 1
                    self.esta_cayendo = False
                    self.en_tierra = True
                    self.lados["main"].bottom = plataforma.lados["main"].top + 1
                    self.corregir_desface_lados()
                    # print("Toco la plataforma")
                    break

                    
            if self.esta_cayendo:
                self.rect.y += 7

                
    
        
        
            


    def movimiento(self,lista_teclas,pantalla):
        if lista_teclas[pygame.K_LEFT]:
            if self.esta_saltando == False:
                self.imagen = personaje_camina_izq
            if not self.toco_lado_izq:
                self.rect.x -= self.velocidad
            self.estado = "izquierda"
            self.orientacion = "izquierda"
        elif lista_teclas[pygame.K_RIGHT]:
            if self.esta_saltando == False:
                self.imagen = personaje_camina_der
            if not self.toco_lado_der:
                self.rect.x += self.velocidad

            self.estado = "derecha"
            self.orientacion = "derecha"
        elif self.esta_saltando == False:
            self.estado = "quieto"
            if self.orientacion == "derecha":
                self.imagen = personaje_quieto_der
            else:
                self.imagen = personaje_quieto_izq


            #print("quieto")


        self.animar(self.imagen,pantalla)


    def resetear_posicion(self,eje_x_eje_y):
        pass


    def verificar_colisiones(self,lista_plataformas,lista_consumibles,lista_enemigos,lista_vidas,lista_enemigos_2):
        self.toco_lado_der = False
        self.toco_lado_izq = False
        self.toco_abajo = False
        for plataforma in lista_plataformas:
            if self.lados['right'].colliderect(plataforma.lados["left"]) and not (self.lados['bottom'].colliderect(plataforma.lados['top'])):
                self.toco_lado_der = True
            if self.lados['left'].colliderect(plataforma.lados["right"]) and not (self.lados['bottom'].colliderect(plataforma.lados['top'])):
                self.toco_lado_izq = True
            if self.lados["top"].colliderect(plataforma.lados["bottom"]):
                self.toco_abajo = True

        for consumible in lista_consumibles:
            if self.rect.colliderect(consumible.rect):
                consumible.se_blitea = False

        for enemigo in lista_enemigos_2:
            if self.lados['bottom'].colliderect(enemigo.lados['top']):
                enemigo.se_blitea = False

        for enemigo in lista_enemigos:
            if self.lados['bottom'].colliderect(enemigo.lados['top']):
                enemigo.se_blitea = False

            for vida in lista_vidas:
                if vida.se_blitea:
                    if self.lados['right'].colliderect(enemigo.lados['left']) or self.lados['left'].colliderect(enemigo.lados['right']):
                        vida.se_blitea = False
                        self.vidas -= 1
                        self.mario_muere = True
                        for lado in self.lados:
                            self.lados[lado].x = 54
                            self.lados[lado].y = 537

                    # mario = Mario(54,537)
                    

                    

        



                
    
            
