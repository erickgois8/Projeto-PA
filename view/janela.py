from tkinter import *

from view.frame_superior import FrameSuperior
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

        # Colocando o frame superior
        self.frame_superior = FrameSuperior(self.root)
        
        # Canvas
        self.area_desenho = AreaDesenho(self.root)

    # ----- Para acesso rápido no controller ----- #

    @property
    def canvas(self):
        return self.area_desenho.canvas
    
    @property
    def botoes_ferramentas(self):
        return self.frame_lateral.frame_ferramentas.botoes_ferramentas
    
    @property
    def botoes_formas(self):
        return self.frame_lateral.frame_formas.botoes_formas
    
    @property
    def botoes_cores(self):
        return self.frame_lateral.frame_cores.botoes_cores
    
    @property
    def botoes_atalhos(self):
        return self.frame_lateral.frame_atalhos.botoes_atalhos
    
    @property
    def botoes_salvar(self):
        return self.frame_superior.botoes_salvar
    
    @property
    def botao_circulo_cromatico(self):
        return self.frame_lateral.frame_cores.botao_cromatico