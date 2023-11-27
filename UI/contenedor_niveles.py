import pygame
from pygame.locals import *

from UI.GUI_form import *
from UI.GUI_button_image import *
from utilidades import *

class FormContenedorNivel(Form):
    def __init__(self,pantalla: pygame.Surface,nivel,datos_jugador,numero_nivel):
        super().__init__(pantalla, 0 , 0, pantalla.get_width(), pantalla.get_height())
        nivel._slave = self._slave
        self.nivel = nivel
        self.estado = "Gano"
        self.flag_guardado = False
        self.datos_jugador = datos_jugador
        self.numero_nivel = numero_nivel
        self._btn_home = Button_Image(screen=self._slave,
                                master_x = self._x,
                                master_y = self._y,
                                x = self._w-70,
                                y = self._h-70,
                                w= 50,
                                h =50,
                                color_background = (255,0,0),
                                color_border = (255,0,255),
                                onclick = self.btn_home_click,
                                onclick_param = "",
                                font = "Verdana",
                                font_size= 23,
                                font_color = (0,255,0),
                                path_image = "Laboratorio2doParcial/fotos/home_white.png")
        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self._btn_home)

    def update(self, lista_eventos):

        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        if self.nivel.flag_gano and self.flag_guardado == False:
            if self.datos_jugador['ultimo_nivel_superado'] < self.numero_nivel:
                self.datos_jugador['ultimo_nivel_superado'] = self.numero_nivel
            self.datos_jugador['puntaje'] += self.nivel.puntaje
            
            guardar_progreso(self.datos_jugador)
            self.flag_guardado = True

           




    def btn_home_click(self,parametro):
        self.end_dialog()
        