from tkinter import *
from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.figuras import Figuras

@dataclass
class FerramentaBorracha(Ferramenta):
    figuras: Figuras
    canvas: Canvas
    raio: int = 3

    def mouse_pressionado(self, event):
        x1 = event.x - self.raio
        y1 = event.y - self.raio
        x2 = event.x + self.raio
        y2 = event.y + self.raio

        ids = self.canvas.find_overlapping(x1, y1, x2, y2)

        for figura in self.figuras.acessar()[:]:
            if figura.id in ids:
                self.figuras.remover(figura)
        
        self.desenho.desenhar_figuras(self.figuras)

    def mouse_arrastado(self, event):
        x1 = event.x - self.raio
        y1 = event.y - self.raio
        x2 = event.x + self.raio
        y2 = event.y + self.raio

        ids = self.canvas.find_overlapping(x1, y1, x2, y2)

        for figura in self.figuras.acessar()[:]:
            if figura.id in ids:
                self.figuras.remover(figura)

        self.desenho.desenhar_figuras(self.figuras)

    def mouse_solto(self, event):
        return