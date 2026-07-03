from figura import Figura
from dataclasses import dataclass, field

@dataclass
class Lapis(Figura):
    pontos: list
    cor_borda: str
    
    def desenhar(self, canvas, dash=()):
        canvas.createline(self.pontos, fill=self.cor_borda, dash=dash)
    
    def incompleta(self):
        return len(self.pontos) <= 1