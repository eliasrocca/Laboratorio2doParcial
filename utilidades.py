import pygame
from configuraciones import *
from modo import *

def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario['main'] = principal
    diccionario['bottom'] = pygame.Rect(principal.left,principal.bottom -15, principal.width, 15)
    diccionario['right'] = pygame.Rect(principal.right - 10, principal.top, 10, principal.height)
    diccionario['left'] = pygame.Rect(principal.left, principal.top , 10, principal.height)
    diccionario['top'] = pygame.Rect(principal.left,principal.top,principal.width,15)
    return diccionario