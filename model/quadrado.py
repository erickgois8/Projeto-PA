from figura import Figura
from dataclasses import dataclass

#Define um quadrado
@dataclass
class Quadrado(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    lado: int = max(abs(x2 - x1), abs(y2 - y1))

# Valida a figura (se os pontos inicial e final coincidem ou não)
    def incompleta(self):
        return (self.x1 == self.x2) and (self.y1 == self.y2)