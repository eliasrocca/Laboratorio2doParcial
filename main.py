import pygame , sys
from pygame.locals import *
from configuraciones import *
from personaje import *
from plataforma import *
from meta import *
from objetos_recolectables import *
from modo import *
from enemigos import *
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from nivel_tres import NivelTres
from UI.GUI_form_principal import *




ANCHO = 1400
ALTO = 700
FPS = 30



PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #px
pygame.display.set_caption("Mario Bros")

form_principal = FormPrincipal(PANTALLA)
# nivel_actual = NivelUno(PANTALLA)

imagen_fondo = pygame.image.load("Laboratorio2doParcial/fotos/fondo_mario.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO,ALTO))

flag_estado = "quieto"
# #MUSICA
# pygame.mixer.music.load('Laboratorio2doParcial/musica_mario.mp3') #ruta de acceso relativa a la cancion
# pygame.mixer.music.play(-1) #el minimo
# pygame.mixer.music.set_volume(0.5) #1 es el maximo, set_volumen sirve para cambiar q tan fuerte suena

clock = pygame.time.Clock()


while True:
    clock.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    PANTALLA.fill("Black")

    # nivel_actual.update(lista_eventos)
    # form_principal.update(lista_eventos)
                
        
    form_principal.update(lista_eventos)

    pygame.display.flip()



    