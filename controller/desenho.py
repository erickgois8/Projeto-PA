from tkinter import *

from model.figura import Figura
from model.lapis import Lapis
from model.linha import Linha
from model.retangulo import Retangulo
from model.quadrado import Quadrado
from model.triangulo import Triangulo
from model.oval import Oval
from model.circulo import Circulo
from model.figuras import Figuras

class Desenho:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas

    # Desenha a nova figura
    def desenhar_figura(self, canvas: Canvas, figura: Figura, dash: tuple=()):
        if isinstance(figura, Lapis):
            figura.id = canvas.create_line(figura.pontos, fill=figura.borda, width=figura.espessura, dash=dash)

        elif isinstance(figura, Linha):
            figura.id = canvas.create_line(figura.pontos, fill=figura.borda, width=figura.espessura, dash=dash)

        elif isinstance(figura, Retangulo):
            figura.id = canvas.create_rectangle(figura.pontos, outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

        elif isinstance(figura, Quadrado):
            figura.id = canvas.create_rectangle(figura.pontos, outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

        elif isinstance(figura, Triangulo):
            figura.id = canvas.create_polygon(figura.pontos, outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

        elif isinstance(figura, Oval):
            figura.id = canvas.create_oval(figura.pontos, outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

        elif isinstance(figura, Circulo):
            figura.id = canvas.create_oval(figura.pontos, outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

    # Permite que tenhamos nossas figuras armazenadas desenhadas e sem rastro
    def redesenhar_figuras(self, canvas: Canvas, figuras: Figuras):
        # Apaga a tela
        canvas.delete("all")

        # Redesenha cada figura a partir dos seus dados
        for i in range(len(figuras.dados)):
            figura = figuras.dados[i]

            # Passamos os dados guardados
            self.desenhar_figura(canvas, figura)