import pygame , sys
from pygame.locals import *
from configuraciones import *
from personaje import *

AZUL = (0,0,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
BLANCO = (255,255,255)


ANCHO = 1400
ALTO = 700
FPS = 30






# def actualizar_pantalla(pantalla , flag_estado , velocidad):
#     pantalla.blit(imagen_fondo,(0,0))
pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #px
pygame.display.set_caption("Mario Bros")



imagen_fondo = pygame.image.load("fotos/fondo_mario.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO,ALTO))

flag_estado = "quieto"

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (ANCHO//2, ALTO//2)


mario = Mario(54,537)


# #MUSICA
# pygame.mixer.music.load('musica_mario.mp3') #ruta de acceso relativa a la cancion
# pygame.mixer.music.play(-1) #el minimo
# pygame.mixer.music.set_volume(0.5) #1 es el maximo, set_volumen sirve para cambiar q tan fuerte suena

clock = pygame.time.Clock()


while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        
    PANTALLA.blit(imagen_fondo , (0,0))
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    # PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)
    
    
    rectangulo_vertical.y += 10
    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0



    if rectangulo_vertical.colliderect(mario.rect):

        imagen_vertical.fill(BLANCO)
    else:
        imagen_vertical.fill(VERDE)


    
    lista_teclas = pygame.key.get_pressed() #para ver q tecla presiono



    mario.update(lista_teclas,PANTALLA)


    # rectangulo_horizontal = personaje_salta[0].get_rect()





    pygame.display.flip()