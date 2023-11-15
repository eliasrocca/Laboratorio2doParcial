import pygame 
from modo import *
import sys
from configuraciones import *
class Nivel:
    def __init__(self, pantalla,personaje_principal,lista_plataformas,imagen_fondo,meta,lista_consumibles,lista_enemigos,lista_vidas,lista_enemigos_2):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.meta = meta
        self.consumibles = lista_consumibles
        self.enemigos = lista_enemigos
        self.vidas = lista_vidas
        self.enemigos_2 = lista_enemigos_2

    def update(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
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
        for plataforma in self.plataformas:
            plataforma.update(self._slave)
            
        self.meta.update(self._slave)
        for consumible in self.consumibles:
            consumible.update(self._slave)


        for enemigo in self.enemigos:
            enemigo.update(self._slave,self.plataformas)

        for enemigo in self.enemigos_2:
            enemigo.update(self._slave,self.plataformas)

        for vida in self.vidas:
            vida.update(self._slave)




        
        lista_teclas = pygame.key.get_pressed() #para ver q tecla presiono



        self.jugador.update(lista_teclas,self._slave, self.plataformas,self.consumibles,self.enemigos,self.vidas,self.enemigos_2)

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo,(0,0))
        
        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas)

        