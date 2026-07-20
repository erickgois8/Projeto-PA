from tkinter import *
from dataclasses import dataclass
from controller.state.ferramenta import Ferramenta
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaBaldeTinta(Ferramenta):
    figuras: Figuras
    estado: Estado
    canvas: Canvas

    def mouse_pressionado(self, event):
        ids = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)

        # O último id retornado pelo canvas é o desenho que está por cima. Assim, o balde altera apenas a figura clicada
        if not ids:
            return

        id_figura = ids[-1]

        for figura in self.figuras.acessar():
            # Linhas e lápis não possuem preenchimento, portanto não devem receber uma cor de preenchimento.
            if figura.id == id_figura and hasattr(figura, "preenchimento"):
                figura.preenchimento = self.estado.cor_preenchimento
                self.desenho.desenhar_figuras(self.figuras)
                return

    def mouse_arrastado(self, event):
        return
    
    def mouse_solto(self, event):
        return
