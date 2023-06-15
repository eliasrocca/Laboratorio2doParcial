import pygame , sys

pygame.init()

PANTALLA = pygame.display.set_mode((500,400)) #px
pygame.display.set_caption("Mario Bros")



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.fill((255,255,255))

    pygame.display.flip()