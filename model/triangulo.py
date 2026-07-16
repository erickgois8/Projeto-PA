from model.figura import Figura
from dataclasses import dataclass

@dataclass
class Triangulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    x3: int
    y3: int

    borda: str
    preenchimento: str
    
    espessura: str

    def incompleta(self):
        return (self.x2 == self.x3) or (self.y1 == self.y2)