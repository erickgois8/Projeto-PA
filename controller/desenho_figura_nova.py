from tkinter import *

from controller.desenho import Desenho, Lapis, Linha, Retangulo, Quadrado, Triangulo, Oval, Circulo, Figuras

class DesenhoFiguraNova:
    def __init__(self, desenho: Desenho, tipo: str, borda: str, preenchimento: str, espessura: int=3):
        # Incluíndo a ferramenta que desenha na tela
        self.desenho = desenho
        self.tipo = tipo
        self.borda = borda
        self.preenchimento = preenchimento
        self.espessura = espessura

    # Quando o mouse é pressionado
    def iniciar(self, event: Event):
        self.figura_nova = None

        # Instancia figuras de cada tipo com base na ferramenta (figura) escolhida
        if self.tipo == "lapis":
            self.figura_nova = Lapis([(event.x, event.y)], self.borda, self.preenchimento, self.espessura)

        elif self.tipo == "linha":
            self.figura_nova == Linha(event.x, event.y, event.x, event.y, self.borda, self.preenchimento, self.espessura)

        elif self.tipo == "retangulo":
            self.figura_nova = Retangulo(event.x, event.y, event.x, event.y, self.borda, self.preenchimento, self.espessura)

        elif self.tipo == "quadrado":
            self.figura_nova = Quadrado(event.x, event.y, event.x, event.y, self.borda, self.preenchimento, self.espessura)

        elif self.tipo == "triangulo":
            self.figura_nova = Triangulo(event.x, event.y, event.x, event.y, self.borda, self.preenchimento, self.espessura)

        elif self.tipo == "oval":
            self.figura_nova = Oval(event.x, event.y, event.x, event.y, self.borda, self.preenchimento, self.espessura)

        elif self.tipo == "circulo":
            self.figura_nova = Circulo(event.x, event.y, event.x, event.y, self.borda, self.preenchimento, self.espessura)
    
    # Quando o mouse é movido
    def atualizar(self, event: Event, canvas: Canvas, figuras: Figuras):

        # LAPIS (Adiciona o ponto pelo qual o mouse passou)
        if self.tipo == "lapis":
            self.figura_nova.pontos.append((event.x, event.y))

        # LINHA (Atualiza o ponto final)
        elif self.tipo == "linha":
            self.figura_nova.x2 = event.x
            self.figura_nova.y2 = event.y

        # RETANGULO (Atualiza o ponto final)
        elif self.tipo == "retangulo":
            self.figura_nova.x2 = event.x
            self.figura_nova.y2 = event.y

        # QUADRADO (Atualiza o lado para conseguir ajustar e atualizar o ponto final)
        elif self.tipo == "quadrado":
            dist_x = event.x - self.figura_nova.x1
            dist_y = event.y - self.figura_nova.y1
            lado = max(abs(dist_x), abs(dist_y)) 
            
            self.figura_nova.x2 = self.figura_nova.x1 + lado * (1 if dist_x >= 0 else -1) 
            self.figura_nova.y2 = self.figura_nova.y1 + lado * (1 if dist_y >= 0 else -1)
        
        # TRIANGULO (Atualiza o ponto final)
        elif self.tipo == "triangulo":
            self.figura_nova.x2 = event.x
            self.figura_nova.y2 = event.y

        # OVAL (Atualiza o ponto final)
        elif self.tipo == "oval":
            self.figura_nova.x2 = event.x
            self.figura_nova.y2 = event.y

        # CIRCULO (Atualiza o ponto final)
        elif self.tipo == "circulo":
            self.figura_nova.x2 = event.x
            self.figura_nova.y2 = event.y

        # Atualiza a tela
        self.desenho.redesenhar_figuras(canvas, figuras)
        self.desenho.desenhar_figura(canvas, self.figura_nova)
    
    # Quando o mouse é solto
    def incluir(self, event: Event, canvas: Canvas, figuras: Figuras): 
        # Verifica se a figura é vazia
        if self.figura_nova is not None:

            # Valida a figura antes de incluir na lista de figuras
            if not self.figura_nova.incompleta():
                figuras.adicionar(self.figura_nova)

        else:
            return

        self.desenho.redesenhar_figuras(canvas, figuras)
