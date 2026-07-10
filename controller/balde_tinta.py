from tkinter import *

from model.figuras import Figuras
from controller.desenho import Desenho

class BaldeTinta:
    def __init__(self, desenho: Desenho):
        self.desenho = desenho
        
    def preencher(self, event: Event, canvas: Canvas, figuras: Figuras, cor_preenchimento: str):
        ids = canvas.find_overlapping(event.x, event.y, event.x, event.y)

        for figura in figuras.dados:
            if figura.id in ids:
                canvas.itemconfig(figura.id, fill=cor_preenchimento)

        self.desenho.redesenhar_figuras(canvas, figuras)