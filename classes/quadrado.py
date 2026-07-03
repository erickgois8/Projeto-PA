from figura import Figura
from dataclasses import dataclass, field

class Quadrado(Figura):
    cor_de_borda: str 
    cor_de_preenchimento: str
    xi: int
    yi: int
    xf: int
    yf: int

    @property
    
    def pontos(self):
        return (self.xi, self.yf, self.xf, self.yf)

    def desenhar (self, canvas, dash=()):
        canvas.create_rectangle(self.pontos, fill = self.cor_preenchimento, outline = self.cor_borda, dash = dash)

    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)