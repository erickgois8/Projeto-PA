from tkinter import *
from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaBaldeTinta(Ferramenta):
    figuras: Figuras
    estado: Estado
    canvas: Canvas

    def mouse_pressionado(self, event):
        ids = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)

        for figura in self.figuras.acessar():
            if figura.id in ids:
                figura.cor_preenchimento = self.estado.cor_preenchimento

        self.desenho.desenhar_figuras(self.figuras)

    def mouse_arrastado(self, event):
        return
    
    def mouse_solto(self, event):
        return