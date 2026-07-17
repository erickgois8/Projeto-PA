from tkinter import *
from model.figuras import Figuras
from model.figura import Figura
from model.lapis import Lapis
from model.linha import Linha
from model.retangulo import Retangulo
from model.quadrado import Quadrado
from model.oval import Oval
from model.circulo import Circulo
from model.triangulo import Triangulo
from model.poligono import Poligono

class Desenho:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas

    # Método para o desenho específico de cada figura
    def desenhar_figura(self, figura: Figura, dash: tuple=()):
        if isinstance(figura, Lapis):
            figura.id = self.canvas.create_line(figura.pontos, fill=figura.borda, width=figura.espessura, dash=dash)

        elif isinstance(figura, Linha):
            figura.id = self.canvas.create_line(figura.x1, figura.y1, figura.x2, figura.y2 ,
                                                fill=figura.borda, width=figura.espessura, dash=dash)

        elif isinstance(figura, Retangulo):
            figura.id = self.canvas.create_rectangle(figura.x1, figura.y1, figura.x2, figura.y2,
                                                    outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

        elif isinstance(figura, Quadrado):
            figura.id = self.canvas.create_rectangle(figura.x1, figura.y1, figura.x2, figura.y2,
                                                    outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

        elif isinstance(figura, Oval):
            figura.id = self.canvas.create_oval(figura.x1, figura.y1, figura.x2, figura.y2,
                                                outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)

        elif isinstance(figura, Circulo):
            figura.id = self.canvas.create_oval(figura.x1 - figura.raio, figura.y1 - figura.raio, figura.x1 + figura.raio, figura.y1 + figura.raio,
                                                outline=figura.borda, fill=figura.preenchimento, width=figura.espessura, dash=dash)
        elif isinstance(figura, Triangulo):
            figura.id = self.canvas.create_polygon(figura.x1, figura.y1, figura.x2, figura.y2, figura.x3, figura.y3,
                                                   outline=figura.borda,fill=figura.preenchimento or "",width=figura.espessura, dash=dash)

        elif isinstance(figura, Poligono):
            figura.id = self.canvas.create_polygon(
                *figura.pontos,
                outline=figura.borda,
                fill=figura.preenchimento or "",
                width=figura.espessura,
                dash=dash,
            )

    def desenhar_figuras(self, figuras: Figuras):
        # Apaga a tela
        self.canvas.delete("all")

        # Redesenha cada figura no canvas
        for figura in figuras.acessar():
            self.desenhar_figura(figura)

    def mover_figura(self, figura: Figura, dx: int, dy: int):
        if isinstance(figura, (Lapis, Poligono)):
            figura.pontos = [(x + dx, y + dy) for x, y in figura.pontos]

        elif isinstance(figura, Triangulo):
            figura.x1 += dx
            figura.y1 += dy
            figura.x2 += dx
            figura.y2 += dy
            figura.x3 += dx
            figura.y3 += dy
            
        else:
            figura.x1 += dx
            figura.y1 += dy
            figura.x2 += dx
            figura.y2 += dy
