from model.figura import Figura
from dataclasses import dataclass

@dataclass
class Retangulo(Figura):
    # Coordenadas
    x1: int
    y1: int
    x2: int
    y2: int

    # Cores
    borda: str
    preenchimento: str
    
    # Espessura
    espessura: str
    
    # Verifica a figura (evitando pontos e retas)
    def incompleta(self):
        return (self.x1 == self.x2) or (self.y1 == self.y2)