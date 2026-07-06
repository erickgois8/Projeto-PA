from figura import Figura
from dataclasses import dataclass

@dataclass
class Triangulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    x3: float = (x2 + x1) / 2
    y3: float = y2

    def incompleta(self):
        return (self.x1 == self.x2) or (self.y1 == self.y2)