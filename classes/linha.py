from figura import Figura
from dataclasses import dataclass, field

@dataclass
class Linha(Figura):
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str

    @property
    def pontos(self):
        return (self.xi, self.yi, self.xf, self.yf)
    
    def desenhar(self, canvas, dash=()):
        canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)

    def incompleta(self):
        (self.xi, self.yi) == (self.xf, self.yf)