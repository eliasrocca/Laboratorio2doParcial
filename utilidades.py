import pygame
from configuraciones import *
from modo import *
import json

def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario['main'] = principal
    diccionario['bottom'] = pygame.Rect(principal.left,principal.bottom -15, principal.width, 15)
    diccionario['right'] = pygame.Rect(principal.right - 10, principal.top, 10, principal.height)
    diccionario['left'] = pygame.Rect(principal.left, principal.top , 10, principal.height)
    diccionario['top'] = pygame.Rect(principal.left,principal.top,principal.width,15)
    return diccionario

def obtener_datos_jugadores():
    try:
        with open('Laboratorio2doParcial/datos_jugadores.json', 'r') as archivo:
            lista_progreso_jugadores = json.load(archivo)

    except:
        lista_progreso_jugadores = []

    return lista_progreso_jugadores


def obtener_progreso(nombre_player):
    try:
        # with open('Laboratorio2doParcial/datos_jugadores.json', 'r') as archivo:
        lista_progreso_jugadores = obtener_datos_jugadores()
        for dato_jugador in lista_progreso_jugadores:
            if nombre_player == dato_jugador['nombre']:
                datos = dato_jugador
                break

        print(datos)
    except:
        datos = {"nombre": nombre_player,
        "puntaje": 0,
        "ultimo_nivel_superado": 0}
        print("no entro")
    return datos

def guardar_progreso(datos_jugador):
        try:
            indice_jugador = -1
            with open('Laboratorio2doParcial/datos_jugadores.json', 'r') as archivo:
                lista_progreso_jugadores = json.load(archivo)
            for i in range(len(lista_progreso_jugadores)):
                if datos_jugador["nombre"] == lista_progreso_jugadores[i]['nombre']:
                    indice_jugador = i
                    break
            if indice_jugador != -1:
                lista_progreso_jugadores[indice_jugador] = datos_jugador
            else:
                lista_progreso_jugadores.append(datos_jugador)

        except:
            lista_progreso_jugadores = [datos_jugador]

        try:  
            with open('Laboratorio2doParcial/datos_jugadores.json', 'w') as archivo:
                json.dump(lista_progreso_jugadores, archivo, indent=4)

        except:
            print("No se pudo guardar el progreso")
        
def obtener_top_jugadores(cantidad):
    lista_scoreboard = []
    lista_progreso_jugadores = obtener_datos_jugadores()
    for i in range(cantidad):
        jugador_top = None
        indice_jugador_top = -1

        for j in range(len(lista_progreso_jugadores)):
            datos_jugador = lista_progreso_jugadores[j]
            if jugador_top == None or datos_jugador['puntaje'] > jugador_top['Puntaje']:
                jugador_top = {'Jugador': datos_jugador['nombre'],'Puntaje': datos_jugador['puntaje']}
                indice_jugador_top = j

        if jugador_top != None:
            lista_scoreboard.append(jugador_top)
            lista_progreso_jugadores.pop(indice_jugador_top)

    return lista_scoreboard

            





