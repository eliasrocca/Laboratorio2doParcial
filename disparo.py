import pygame

class Disparo:
    def __init__(self,x,y,direccion):
        self.superficie = pygame.image.load("Laboratorio2doParcial/fotos/ataque_boss_der_2.png")
        self.superficie = pygame.transform.scale(self.superficie, (70,40))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion 
        self.se_blitea = True


    def update(self,pantalla,personaje,lista_vidas):
        if self.se_blitea:
            ancho_pantalla = pantalla.get_width()
            pantalla.blit(self.superficie,self.rectangulo)
            if self.direccion == "derecha" or self.direccion == "quieto":
                self.rectangulo.x += 10
            elif self.direccion == "izquierda":
                self.rectangulo.x -= 10

            if self.rectangulo.centerx < 0 or self.rectangulo.centerx > ancho_pantalla:
                self.se_blitea = False


            if self.rectangulo.colliderect(personaje.rect):
                self.se_blitea = False
                personaje.recibir_daño(lista_vidas)




    
            
    
    
