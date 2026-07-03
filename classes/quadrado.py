from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Quadrado(Figura):
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str 
    cor_preenchimento: str

    @property
    def pontos(self):
        return (self.xi, self.yi, self.xf, self.yf)

    def desenhar(self, canvas, dash=()):
        canvas.create_rectangle(self.pontos, fill=self.cor_preenchimento, outline = self.cor_borda, dash=dash)

    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)
    
    def atualizar(self, event):
        self.dist_x = event.x - self.xi 
        self.dist_y = event.y - self.yi
        lado = max(abs(self.dist_x), abs(self.dist_y)) 
        self.xf = self.xi + lado * (1 if self.dist_x >= 0 else -1) 
        self.yf = self.yi + lado * (1 if self.dist_y >= 0 else -1)