import pygame, sys
from pygame.locals import *
# from Imagen_2 import Imagen

ANCHO = 1400
ALTO = 700
FPS = 30

pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #px
pygame.display.set_caption("Mario Bros")

#MUSICA
#pygame.mixer.music.load('INTRO PYGAME/Recursos/intro.mp3') #ruta de acceso relativa a la cancion
#pygame.mixer.music.play(-1) #rep la musica en bucle
#pygame.mixer.music.set_volume(0.5) #1 es el maximo, set_volumen sirve para cambiar q tan fuerte suena

#icono = pygame.image.load('INTRO PYGAME\Recursos\icono_homero.png') #cargamos la imagen del icono
#pygame.display.set_icon(icono)

#para hacer el fondo
imagen_mario = pygame.image.load("141.png")
imagen_mario = pygame.transform.scale(imagen_mario,(55,70))

imagen_fondo = pygame.image.load("fondo_mario.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO,ALTO))






clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_UP:
                imagen_mario.mover_imagen('Vertical', -10, (ANCHO, ALTO))
            elif evento.key == K_DOWN:
                imagen_mario.mover_imagen('Vertical', 10, (ANCHO, ALTO))
            elif evento.key == K_LEFT:
                imagen_mario.mover_imagen('Horizontal', -10, (ANCHO, ALTO))
            elif evento.key == K_RIGHT:
                imagen_mario.mover_imagen('Horizontal', 10, (ANCHO, ALTO))

    lista_teclas = pygame.key.get_pressed() #para ver q tecla presiono
    if lista_teclas[pygame.K_0]: #pongo lo q quiero q haga en cuanto a la tecla presionada
        print('0')
    if lista_teclas[pygame.K_LEFT]:
        print('izquierda')
    if lista_teclas[pygame.K_RIGHT]:
        print ('derecha')
    if lista_teclas[pygame.K_ESCAPE]:
        flag = False

    PANTALLA.blit (imagen_fondo, (0,0))

    # PANTALLA.blit(imagen_vertical.imagen, imagen_vertical.rectangulo) 
    PANTALLA.blit(imagen_mario.imagen, imagen_mario.rectangulo)

    # imagen_vertical.mover_imagen('Vertical', 10, (ANCHO, ALTO))
    imagen_mario.mover_imagen('Horizontal', 10, (ANCHO,ALTO))

    # imagen_horizontal.detectar_colision(imagen_vertical)


    pygame.display.flip()