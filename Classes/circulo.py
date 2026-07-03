from figura import Figura
from dataclasses import dataclass, field

@dataclass
class Circulo(Figura):
    cor_borda: str
    cor_preenchimento: str
    xi: int
    yi: int
    xf: int
    yf: int
    raio: float

    def desenhar(self, canvas, dash=()):
        self.raio = ((self.yf - self.yi) ** 2 + (self.xf - self.xi) ** 2) ** 0.5
        canvas.create_oval(self.xi - self.raio, self.yi - self.raio, self.xi + self.raio, self.yi + self.raio,
                            fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash)
        
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)