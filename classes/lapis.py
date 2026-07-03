from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Lapis(Figura):
    pontos: list
    cor_borda: str
    
    def desenhar(self, canvas, dash=()):
        canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)
    
    def incompleta(self):
        return len(self.pontos) <= 1
    
    def atualizar(self, event):
        self.pontos.append((event.x, event.y))
