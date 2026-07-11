from tkinter import *
from controller.controller_principal import Figuras, Figura, Lapis, Linha, Retangulo, Quadrado, Oval, Circulo

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
    
    def desenhar_figuras(self, figuras: Figuras):
        # Apaga a tela
        self.canvas.delete("all")

        # Redesenha cada figura no canvas
        for figura in figuras.acessar:
            self.desenhar_figura(figura)