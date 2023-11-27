from pygame.locals import *
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from nivel_tres import NivelTres

class Manejador_niveles:
    def __init__(self,pantalla) -> None:
        self._slave = pantalla
        self.niveles = {1: NivelUno, 2: NivelDos, 3: NivelTres}

    def get_nivel(self,nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
