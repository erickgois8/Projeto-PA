from tkinter import *

from model.figuras import Figuras
from controller.desenho import Desenho

class Borracha:
    def __init__(self, desenho: Desenho, raio: int=3):
        self.raio = raio
        self.desenho = desenho

    def apagar(self, event, canvas: Canvas, figuras: Figuras):
    
        x1 = event.x - self.raio
        y1 = event.y - self.raio
        x2 = event.x + self.raio
        y2 = event.y + self.raio

        ids = canvas.find_overlapping(x1, y1, x2, y2)

        for figura in figuras.dados[:]:
            if figura.id in ids:
                figuras.remover(figura)
            
        self.desenho.redesenhar_figuras(canvas, figuras)


















