from figura import Figura
from dataclasses import dataclass

@dataclass
class Oval(Figura):
    x1: int
    y1: int
    x2: int
    y2: int

    def incompleta(self):
        return (self.x1 == self.x2) or (self.y1 == self.y2)