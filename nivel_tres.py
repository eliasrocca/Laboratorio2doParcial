from configuraciones import *
import pygame
from pygame.locals import *
from modo import *
from objetos_recolectables import *
from meta import * 
from enemigos import *
from nivel import Nivel
from plataforma import *
from personaje import *
from enemigos_estaticos import *
from jefe import *

class NivelTres(Nivel):
    def __init__(self,pantalla: pygame.Surface):
        # AZUL = (0,0,255)
        # NEGRO = (0,0,0)
        # ROJO = (255,0,0)
        # VERDE = (0,255,0)
        # BLANCO = (255,255,255)

        W = pantalla.get_width()
        H = pantalla.get_height()


        BG = pygame.image.load("Laboratorio2doParcial/fotos/BG_BLACK.png")
        BG = pygame.transform.scale(BG,(W,H))



        # def actualizar_pantalla(pantalla , flag_estado , velocidad):
        #     pantalla.blit(imagen_fondo,(0,0))
        

        
        pygame.display.set_caption("Mario Bros")



        imagen_fondo = pygame.image.load("Laboratorio2doParcial/fotos/fondo_mario.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo,(W,H))

        # flag_estado = "quieto"




        mario = Mario(54,537)

        plataforma_1 = Plataforma(350,415,45,45,"Laboratorio2doParcial/fotos/0.png")
        # plataforma_2 = Plataforma(395,415,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_3 = Plataforma(650,462,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_4 = Plataforma(695,462,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_5 = Plataforma(950,415,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_6 = Plataforma(995,415,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_7 = Plataforma(740,462,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_8 = Plataforma(605,462,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_9 = Plataforma(1150,355,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_10 = Plataforma(1195,355,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_11 = Plataforma(225,355,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_12 = Plataforma(180,355,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_13 = Plataforma(50,260,45,45,"Laboratorio2doParcial/fotos/0.png")


        meta = Meta(1125,55,100,300,"Laboratorio2doParcial/fotos/Bandera_definitiva.webp")
        consumibles = Consumible(1180,562,45,45,"Laboratorio2doParcial/fotos/estrella_coronativa.webp")
        consumible_2 = Consumible(50,215,45,45,"Laboratorio2doParcial/fotos/estrella_coronativa.webp")
        vida_1 = Consumible(1320,20,40,40,"Laboratorio2doParcial/fotos/vidas_mario.webp")
        vida_2 = Consumible(1280,20,40,40,"Laboratorio2doParcial/fotos/vidas_mario.webp")
        vida_3 = Consumible(1240,20,40,40,"Laboratorio2doParcial/fotos/vidas_mario.webp")
        self.jefe = Jefe(675,510,100,100,"Laboratorio2doParcial/fotos/boss_der_4.png")
        enemigo_3 = Enemigo(675,423,40,40,"Laboratorio2doParcial/fotos/enemigo_2_dif.png")
        # enemigo_2 = Enemigo_estatico(1075,550,60,60,"Laboratorio2doParcial/fotos/enemigo_planta_1.png")



        plataforma_piso = Plataforma(0,605,1400,100)


        lista_plataformas = [plataforma_piso,plataforma_1,plataforma_8,plataforma_11,plataforma_12,plataforma_3,plataforma_4,plataforma_5,
                            plataforma_6,plataforma_7,plataforma_9,plataforma_10,plataforma_13
                            ]

        lista_consumibles = [consumibles,consumible_2]

        lista_enemigos = [self.jefe,enemigo_3]

        

        lista_vidas = [vida_1,vida_2,vida_3]
        super().__init__(pantalla,mario,lista_plataformas,imagen_fondo,meta,lista_consumibles,lista_enemigos,lista_vidas)

    def verificar_gano_nivel(self):
        if self.jugador.rect.colliderect(self.meta) and self.jefe.se_blitea == False:
            self.flag_gano = True