import pygame 
from modo import *
import sys
from configuraciones import *
from jefe import *
import json

class Nivel:
    def __init__(self, pantalla,personaje_principal,lista_plataformas,imagen_fondo,meta,lista_consumibles,lista_enemigos,lista_vidas):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.meta = meta
        self.consumibles = lista_consumibles
        self.enemigos = lista_enemigos
        self.vidas = lista_vidas
        self.flag_gano = False
        self.imagen_ganaste = pygame.image.load("Laboratorio2doParcial/fotos/level_completed.png")
        self.imagen_ganaste = pygame.transform.scale(self.imagen_ganaste,(self._slave.get_width(),self._slave.get_height()))
        self.puntaje = 0
        self.fuente =  pygame.font.Font(None, 28)
        self.texto = self.fuente.render(f"Score: {self.puntaje}", True, "white")
        

    def update(self,lista_eventos):
        self.verificar_gano_nivel()
        if self.flag_gano == False:
            self.texto = self.fuente.render(f"Score: {self.puntaje}", True, "white")
            self.sumar_puntos()
            for evento in lista_eventos:

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    print(evento.pos)
                elif evento.type == pygame.KEYDOWN:
                    if self.jugador.en_tierra and evento.key == pygame.K_UP:
                        self.jugador.en_tierra = False
                        if self.jugador.orientacion == "derecha":
                            self.jugador.imagen = personaje_salta_der
                        elif self.jugador.orientacion == "izquierda":
                            self.jugador.imagen = personaje_salta_izq
                            
                        print(self.jugador.rect.y)
                        #self.rect.y -= 60
                        self.jugador.estado = "salto"
                        self.jugador.esta_saltando = True
                    elif evento.key == pygame.K_TAB:
                        cambiar_modo()
                    

            

            self._slave.blit(self.img_fondo , (0,0))
            self._slave.blit(self.texto, (20,25))
            for plataforma in self.plataformas:
                plataforma.update(self._slave)
                
            self.meta.update(self._slave)
            for consumible in self.consumibles:
                consumible.update(self._slave)


            for enemigo in self.enemigos:
                if type(enemigo) == Jefe:
                    enemigo.update(self._slave,self.plataformas,self.jugador,self.vidas)
                else:
                    enemigo.update(self._slave,self.plataformas)



            for vida in self.vidas:
                vida.update(self._slave)



            # if self.jugador['right'].colliderect(self.meta['left']) or self.jugador['left'].colliderect(self.meta['right']):
            #     print("colisiono")
            
            lista_teclas = pygame.key.get_pressed() #para ver q tecla presiono



            self.jugador.update(lista_teclas,self._slave, self.plataformas,self.consumibles,self.enemigos,self.vidas,self.meta)

        else:
            self._slave.blit(self.imagen_ganaste,(0,0))

            

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo,(0,0))
        
        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas)

        
    def verificar_gano_nivel(self):
        pass
        

    def sumar_puntos(self):
        self.puntaje += self.jugador.puntos_sumados
        self.jugador.puntos_sumados = 0