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

class NivelUno(Nivel):
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
        plataforma_2 = Plataforma(395,415,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_3 = Plataforma(650,485,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_4 = Plataforma(695,485,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_5 = Plataforma(950,415,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_6 = Plataforma(995,415,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_7 = Plataforma(740,485,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_8 = Plataforma(605,485,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_9 = Plataforma(1150,355,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_10 = Plataforma(1195,355,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_11 = Plataforma(225,355,45,45,"Laboratorio2doParcial/fotos/0.png")
        plataforma_12 = Plataforma(180,355,45,45,"Laboratorio2doParcial/fotos/0.png")

        meta = Meta(155,55,100,300,"Laboratorio2doParcial/fotos/Bandera_definitiva.webp")
        consumibles = Consumible(1170,310,45,45,"Laboratorio2doParcial/fotos/estrella_coronativa.webp")
        vida_1 = Consumible(1320,20,40,40,"Laboratorio2doParcial/fotos/vidas_mario.webp")
        vida_2 = Consumible(1280,20,40,40,"Laboratorio2doParcial/fotos/vidas_mario.webp")
        vida_3 = Consumible(1240,20,40,40,"Laboratorio2doParcial/fotos/vidas_mario.webp")
        enemigo_1 = Enemigo(675,567,40,40,"Laboratorio2doParcial/fotos/enemigo_1.png")
        enemigo_2 = Enemigo(675,446,40,40,"Laboratorio2doParcial/fotos/enemigo_1.png")


        plataforma_piso = Plataforma(0,605,1400,100)


        lista_plataformas = [plataforma_piso,plataforma_1,plataforma_2,plataforma_3,plataforma_4,plataforma_5,
                            plataforma_6,plataforma_7,plataforma_8,plataforma_9,plataforma_10,
                            plataforma_11,plataforma_12]

        lista_consumibles = [consumibles]

        lista_enemigos = [enemigo_1,enemigo_2]

        lista_enemigos_2 = []

        

        lista_vidas = [vida_1,vida_2,vida_3]
        super().__init__(pantalla,mario,lista_plataformas,imagen_fondo,meta,lista_consumibles,lista_enemigos,lista_vidas,lista_enemigos_2)
        