import pygame 





ANCHO = 1400
ALTO = 700
FPS = 30


pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #px
pygame.display.set_caption("Mario Bros")



flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos) #sirve para saber donde poner las medidas de la pantalla en vez de ir tirando por tirar

    lista_teclas = pygame.key.get_pressed() #para ver q tecla presiono
    if lista_teclas[pygame.K_0]: #pongo lo q quiero q haga en cuanto a la tecla presionada
        print('0')
    if lista_teclas[pygame.K_LEFT]:
        print('izquierda')
    if lista_teclas[pygame.K_RIGHT]:
        print ('derecha')
    if lista_teclas[pygame.K_ESCAPE]:
        flag = False
    pygame.display.update()
pygame.quit()



