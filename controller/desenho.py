from model.lapis import Lapis
from model.linha import Linha
from model.retangulo import Retangulo
from model.quadrado import Quadrado
from model.triangulo import Triangulo
from model.oval import Oval
from model.circulo import Circulo

class Desenho:
    def __init__(self, canvas):
        self.canvas = canvas

    # Desenha a nova figura
    def desenhar_figura(self, canvas, figura, borda, preenchimento, espessura, dash=()):
        if isinstance(figura, Lapis):
            figura.id = canvas.create_line(figura.pontos, fill=borda, width=espessura, dash=dash)

        elif isinstance(figura, Linha):
            figura.id = canvas.create_line(figura.x1, figura.y1, figura.x2, figura.y2, fill=borda, width=espessura, dash=dash)

        elif isinstance(figura, Retangulo):
            figura.id = canvas.create_rectangle(figura.x1, figura.y1, figura.x2, figura.y2, outline=borda, fill=preenchimento, width=espessura, dash=dash)

        elif isinstance(figura, Quadrado):
            figura.id = canvas.create_rectangle(figura.x1, figura.y1, figura.x2, figura.y2, outline=borda, fill=preenchimento, width=espessura, dash=dash)

        elif isinstance(figura, Triangulo):
            figura.id = canvas.create_polygon(figura.x1, figura.y1, figura.x2, figura.y2, figura.x3, figura.y3, outline=borda, fill=preenchimento, width=espessura, dash=dash)

        elif isinstance(figura, Oval):
            figura.id = canvas.create_oval(figura.x1, figura.y1, figura.x2, figura.y2, outline=borda, fill=preenchimento, width=espessura, dash=dash)

        elif isinstance(figura, Circulo):
            figura.id = canvas.create_oval(figura.x1, figura.y1, figura.x2, figura.y2, outline=borda, fill=preenchimento, width=espessura, dash=dash)

    # Permite que tenhamos nossas figuras armazenadas desenhadas e sem rastro
    def redesenhar_figuras(self, canvas, figuras):
        canvas.delete("all")

        for figura in figuras:
            self.desenhar_figura(canvas, figura)