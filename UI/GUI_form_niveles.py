import pygame
from pygame.locals import *

from UI.GUI_button_image import *
from UI.GUI_form import *
from UI.GUI_label import *
from UI.GUI_picture_box import *
from UI.manejador_niveles import Manejador_niveles
from UI.contenedor_niveles import *

        
class FormMenuNiveles(Form):
    def __init__(self, screen,path_image,datos_jugador):
        ancho_pantalla = screen.get_width()
        h = screen.get_height()
        w = 400
        x = ancho_pantalla / 2 - w/2
        y = 0
        super().__init__(screen, x,y,w,h)
        self.manejador_niveles = Manejador_niveles(self._master)
        self.lista_widgets = []
        self.datos_jugador = datos_jugador
        self.imagen_fondo = PictureBox(self._slave,0,0,w,h,path_image)

        self.boton_nivel_uno = Button_Image(self._slave,x,y,110,180,100,100,"Laboratorio2doParcial/fotos/nivel_1.png",self.cambiar_nivel,1)
        self.boton_nivel_dos = Button_Image(self._slave,x,y,220,180,100,100,"Laboratorio2doParcial/fotos/nivel_2.png",self.cambiar_nivel,2)
        self.boton_nivel_tres = Button_Image(self._slave,x,y,165,285,100,100,"Laboratorio2doParcial/fotos/nivel_3.png",self.cambiar_nivel,3)

        #Crear boton home
        self._btn_home = Button_Image(screen=self._slave,
                                      x = w-70,
                                      y = h-70,
                                      master_x = x,
                                      master_y = y,
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
        
        self.lista_widgets.append(self.imagen_fondo)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.boton_nivel_uno)
        self.lista_widgets.append(self.boton_nivel_dos)
        self.lista_widgets.append(self.boton_nivel_tres)
        
    def btn_home_click(self,parametro):
        self.end_dialog()
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self._master.fill("black")
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()

        else:
            self.hijo.update(lista_eventos)
                
    def cambiar_nivel(self,nivel_int):
        nivel_max_habilitado = self.datos_jugador['ultimo_nivel_superado'] + 1
        if nivel_int <= nivel_max_habilitado:

            nivel = self.manejador_niveles.get_nivel(nivel_int)
            form_contenedor_nivel = FormContenedorNivel(self._master,nivel,self.datos_jugador,nivel_int)
            self.show_dialog(form_contenedor_nivel)



                
