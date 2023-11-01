import pygame

class Mario:
    def __init__(self,eje_x,eje_y) -> None:
        self.velocidad = 7
        self.estado = "quieto"
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
        self.contador_pasos = 0
        self.imagen_izq = [imagen_mario_izq]
        self.imagen_der = [imagen_mario_der]
        self.imagen_salto_der = [imagen_mario_salto_der]
        self.imagen_salto_izq = [imagen_mario_salto_izq]
        
        
        self.imagen = [imagen_mario]
        self.rect = self.imagen[0].get_rect()
        self.rect.x = eje_x
        self.rect.y = eje_y

    def update(self,lista_teclas,pantalla):
        self.movimiento(lista_teclas,pantalla)

    def animar(self,lista_imagenes,pantalla):
        largo = len(lista_imagenes)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(lista_imagenes[self.contador_pasos],self.rect)
        self.contador_pasos += 1
    

    def movimiento(self,lista_teclas,pantalla):
        if lista_teclas[pygame.K_LEFT]:
            self.imagen = self.imagen_izq
            self.rect.x -= self.velocidad
            self.estado = "izquierda"
        elif lista_teclas[pygame.K_RIGHT]:
            self.imagen = self.imagen_der
            self.rect.x += self.velocidad
            self.estado = "derecha"
        elif lista_teclas[pygame.K_UP]:
            self.imagen = self.imagen_salto_der
            
            self.rect.y -= self.velocidad
            self.estado = "salto"
        else:
            self.estado = "quieto"
            print("quieto")


        self.animar(self.imagen,pantalla)

