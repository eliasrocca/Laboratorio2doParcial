import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from UI.GUI_form_menu_score import *
from UI.GUI_form_niveles import *
from utilidades import *


    
class FormPrincipal(Form):
    def __init__(self, screen):
        x = 200
        y = 100
        w = 900
        h = 350
        color_background = "black"
        color_border = "Magenta"
        border_size = 5
        
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size)

        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()

        self.txtbox = TextBox(self._slave, x , y, 375, 70 , 150, 30, "Gray", "White","Red", "Blue",2,font = "Comic Sans", font_size = 15, font_color = "Black")
        self.btn_play = Button(self._slave,x,y,400,250,100,50,"Red","Blue",self.btn_play_click,"Nombre","Pause", font = "Verdana", font_size = 15, font_color= "White")
        self.label_volumen = Label(self._slave,105,305,30,30,"20%","Comic Sans",15,"Red","Laboratorio2doParcial/fotos/table_png.png")
        self.slider_volumen = Slider(self._slave,x,y,20,280,200,15,self.volumen,"Blue","White",)
        self.btn_tabla = Button_Image(self._slave,x,y,825,260,50,50,"Laboratorio2doParcial/fotos/boton_menu.webp",self.btn_tabla_click,"lalal")
        self.btn_jugar = Button_Image(self._slave,x,y,755,260,50,50,"Laboratorio2doParcial/fotos/boton_niveles.png",self.btn_jugar_click,"Coronacion absoluta")

        self.imagen_bg = PictureBox(self._slave,275,0,350,h,"Laboratorio2doParcial/fotos/mario_menu.jpg")


        self.lista_widgets.append(self.imagen_bg)
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self._master.fill("black")
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
        
    
    def btn_play_click(self, param):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play
    
    
    def btn_tabla_click(self, param):
        ancho_pantalla = self._master.get_width()
        alto_pantalla = self._master.get_height()
        w = 500
        h = 550
        x = ancho_pantalla / 2 - w/2
        y = alto_pantalla /2 - h/2
        dic_score = obtener_top_jugadores(3)
        print(dic_score)
        form_puntaje = FormMenuScore(self._master,
                                     x,
                                     y,
                                     w,
                                     h,
                                     (220,0,220),
                                     "White",
                                     True,
                                     "Laboratorio2doParcial/fotos/window_score.png",
                                     dic_score,
                                     100,
                                     10,
                                     10
                                     )
        
        self.show_dialog(form_puntaje)

    def btn_jugar_click(self, param):
        nombre_player = self.txtbox.get_text()
        nombre_player = nombre_player.strip()
        nombre_player = nombre_player.title()
        if nombre_player != "":
            datos_jugador = obtener_progreso(nombre_player)
            form_jugar = FormMenuNiveles(self._master,"Laboratorio2doParcial/fotos/fondo_menu_jugar.jpg",datos_jugador)
            self.show_dialog(form_jugar)
