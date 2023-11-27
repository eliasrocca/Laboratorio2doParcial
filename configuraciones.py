import pygame

personaje_quieto_izq = [pygame.image.load("Laboratorio2doParcial/fotos/140.png")]

personaje_quieto_der = [pygame.image.load("Laboratorio2doParcial/fotos/141.png")]

personaje_camina_izq = [pygame.image.load("Laboratorio2doParcial/fotos/140.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/140.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/140.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/140.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/139.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/139.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/139.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/139.png")]
                        

personaje_camina_der = [pygame.image.load("Laboratorio2doParcial/fotos/142.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/142.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/142.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/142.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/141.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/141.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/141.png"),
                        pygame.image.load("Laboratorio2doParcial/fotos/141.png")]

personaje_salta_izq = [pygame.image.load("Laboratorio2doParcial/fotos/143.png")]

personaje_salta_der = [pygame.image.load("Laboratorio2doParcial/fotos/146.png")]

personaje_movilidad = [pygame.image.load("Laboratorio2doParcial/fotos/139.png"),
                    pygame.image.load("Laboratorio2doParcial/fotos/142.png")]

lista_general = [personaje_quieto_izq,personaje_quieto_der,
                personaje_camina_izq,personaje_camina_der,
                personaje_salta_izq,personaje_salta_der,personaje_movilidad]

boss_quieto_izq = [pygame.image.load("Laboratorio2doParcial/fotos/boss_izq.png")]
boss_quieto_der = [pygame.image.load("Laboratorio2doParcial/fotos/boss_der.png")]

boss_camina_izq = [pygame.image.load("Laboratorio2doParcial/fotos/boss_izq_4.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_izq_4.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_izq_3.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_izq_3.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_izq_2.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_izq_2.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_izq.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_izq.png")
                ]

boss_camina_der = [pygame.image.load("Laboratorio2doParcial/fotos/boss_der_2.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_der_2.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_der_2.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_der_2.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_der.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_der.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_der_4.png"),
                pygame.image.load("Laboratorio2doParcial/fotos/boss_der_4.png")
                ]

lista_general_boss = [boss_quieto_izq,boss_quieto_der,boss_camina_der,boss_camina_izq]


def reescalar_imagenes_mario(ancho,alto):
    for lista in lista_general:
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i],(ancho,alto))


def reescalar_imagenes_boss(ancho,alto):
    for lista in lista_general_boss:
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i],(ancho,alto))

