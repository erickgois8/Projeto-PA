from model.figura import Figura
from dataclasses import dataclass

#Define um quadrado
@dataclass
class Quadrado(Figura):
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

    # Verifica a figura (evitando pontos)
    def incompleta(self):
        return (self.x1 == self.x2) and (self.y1 == self.y2)