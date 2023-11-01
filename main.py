import pygame , sys
from pygame.locals import *
from configuraciones import *

AZUL = (0,0,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
BLANCO = (255,255,255)


ANCHO = 1400
ALTO = 700
FPS = 30


def mover_personaje(rectangulo_horizontal, velocidad):
    rectangulo_horizontal.x += velocidad



# def actualizar_pantalla(pantalla , flag_estado , velocidad):
#     pantalla.blit(imagen_fondo,(0,0))
pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #px
pygame.display.set_caption("Mario Bros")

imagen_mario = pygame.image.load("fotos/141.png")
imagen_mario_izq = pygame.image.load("fotos/140.png")
imagen_mario_der = pygame.image.load("fotos/141.png")
imagen_mario_salto_der = pygame.image.load("fotos/146.png")
imagen_mario_salto_izq = pygame.image.load("fotos/143.png")
imagen_mario = pygame.transform.scale(imagen_mario,(55,70))
imagen_mario_izq = pygame.transform.scale(imagen_mario_izq,(55,70))
imagen_mario_der = pygame.transform.scale(imagen_mario_der,(55,70))
imagen_mario_salto_izq = pygame.transform.scale(imagen_mario_salto_izq,(55,70))
imagen_mario_salto_der = pygame.transform.scale(imagen_mario_salto_der,(55,70))


imagen_fondo = pygame.image.load("fotos/fondo_mario.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO,ALTO))

flag_estado = "quieto"

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (ANCHO//2, ALTO//2)

imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL)

rectangulo_horizontal = imagen_mario.get_rect()
rectangulo_horizontal.bottom = 607
rectangulo_horizontal.left = 54



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
    PANTALLA.blit(imagen_mario, rectangulo_horizontal)
    
    rectangulo_vertical.y += 10
    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0



    if rectangulo_vertical.colliderect(rectangulo_horizontal):
        imagen_horizontal.fill(ROJO)
        imagen_vertical.fill(BLANCO)
    else:
        imagen_vertical.fill(VERDE)
        imagen_horizontal.fill(AZUL)

    
    lista_teclas = pygame.key.get_pressed() #para ver q tecla presiono

    if lista_teclas[pygame.K_LEFT]:
        imagen_mario = imagen_mario_izq
        print('izquierda')
        flag_estado = "izquierda"
    elif lista_teclas[pygame.K_RIGHT]:
        imagen_mario = imagen_mario_der
        print ('derecha')
        flag_estado = "derecha"
    elif lista_teclas[pygame.K_UP]:
        imagen_mario = imagen_mario_salto_der
        
        print("salto")
        flag_estado = "salto"
    else:
        flag_estado = "quieto"
        print("quieto")
    if lista_teclas[pygame.K_ESCAPE]:
        flag = False

    if flag_estado == "izquierda":
        nueva_x = rectangulo_horizontal.x-10
        if nueva_x > 0 and nueva_x < ANCHO:
            rectangulo_horizontal.x -= 10
    elif flag_estado == "derecha":
        nueva_x = rectangulo_horizontal.x+10 
        if nueva_x > 0 and nueva_x < ANCHO - rectangulo_horizontal.width:
            rectangulo_horizontal.x += 10
    elif flag_estado == "salto":
        rectangulo_horizontal.y -= 10
    else:
        pass

    #personaje
    contador_pasos = 0
    x_inicial = ANCHO/2 - 300
    y_inicial = 650
    posicion_actual_x = 0
    velocidad = 10

    lista_imagenes = [personaje_quieto,personaje_camina,personaje_salta]
    # rectangulo_horizontal = personaje_salta[0].get_rect()





    pygame.display.flip()