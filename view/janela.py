from tkinter import *

from view.frame_lateral import FrameLateral
from view.area_desenho import AreaDesenho

class Janela:
    def __init__(self):
        self.root = Tk()

        # Título e dimensão da janela
        self.root.title("Meu paint")
        self.root.geometry("1920x1080")

        # Colocando frame lateral
        self.frame_lateral = FrameLateral(self.root)
        
        # Canvas
        self.area_desenho = AreaDesenho(self.root)

    @property
    def canvas(self):
        return self.area_desenho.canvas