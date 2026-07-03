from figura import Figura
from dataclasses import dataclass, field

class Oval(Figura):
    cor_de_borda: str
    cor_de_preenchimento: str
    xi: int
    yi: int
    xf: int
    yf: int

    def desenhar(self, canvas, dash=()):
        return canvas.create_oval(self.xi, self.yi, self.xy, self.yf,
                                   fill = self.cor_de_preenchimento, outline = self.cor_de_borda, dash = dash)
    
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)