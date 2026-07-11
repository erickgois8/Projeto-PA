from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Quadrado(Figura):

    # Coordenadas dos pontos inicial e final, além da cor da borda e preenchimento da figura
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str 
    cor_preenchimento: str

    # Desenha a figura baseada no ponto inicial, final e tamanho de lado
    def desenhar(self, canvas, dash=()):
        self.tipo = "quadrado"
        self.id = canvas.create_rectangle(self.xi, self.yi, self.xf, self.yf, fill=self.cor_preenchimento, outline = self.cor_borda, dash=dash, width=3)

    # Atualiza def a figura conforme o tamanho varia o o ponto final e o lado
    def atualizar(self, event):
        self.dist_x = event.x - self.xi 
        self.dist_y = event.y - self.yi
        lado = max(abs(self.dist_x), abs(self.dist_y)) 
        self.xf = self.xi + lado * (1 if self.dist_x >= 0 else -1) 
        self.yf = self.yi + lado * (1 if self.dist_y >= 0 else -1)

        
        
    # Valida a figura (se os pontos inicial e final coincidem ou não)
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)