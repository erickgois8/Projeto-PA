from figura import Figura
from dataclasses import dataclass

@dataclass
class Circulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    raio: float = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

    def incompleta(self):
        return (self.x1 == self.x2) and (self.y1 == self.y2)