import pygame , sys
AZUL = (0,0,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
BLANCO = (255,255,255)


ANCHO = 800
ALTO = 600
FPS = 30


pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #px
pygame.display.set_caption("Mario Bros")

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (ANCHO//2, ALTO//2)

imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL)

rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (ANCHO//2, ALTO//2)

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    PANTALLA.fill(NEGRO)
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    rectangulo_vertical.y += 10
    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)
    if rectangulo_horizontal.left > ANCHO:
        rectangulo_horizontal.right = 0
    rectangulo_horizontal.x += 10



    pygame.display.flip()


