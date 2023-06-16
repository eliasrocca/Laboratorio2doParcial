import pygame , sys
AZUL = (0,0,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
BLANCO = (255,255,255)


ANCHO = 1400
ALTO = 700
FPS = 30


pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #px
pygame.display.set_caption("Mario Bros")

imagen_mario = pygame.image.load("141.png")
imagen_mario = pygame.transform.scale(imagen_mario,(55,70))

imagen_fondo = pygame.image.load("fondo_mario.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO,ALTO))

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (ANCHO//2, ALTO//2)

imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL)

rectangulo_horizontal = imagen_mario.get_rect()
rectangulo_horizontal.bottom = 607
rectangulo_horizontal.left = 54

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

    rectangulo_horizontal.x += 10
    if rectangulo_horizontal.left > ANCHO:
        rectangulo_horizontal.right = 0

    if rectangulo_vertical.colliderect(rectangulo_horizontal):
        imagen_horizontal.fill(ROJO)
        imagen_vertical.fill(BLANCO)
    else:
        imagen_vertical.fill(VERDE)
        imagen_horizontal.fill(AZUL)



    pygame.display.flip()