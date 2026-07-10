from model.figura import Figura
from dataclasses import dataclass

@dataclass
class Triangulo(Figura):
    # Coordenadas
    x1: int
    y1: int
    x2: int
    y2: int

    # Cores
    borda: str
    preenchimento: str
    
    # espessura
    espessura: str

    # Identifica a figura para desenho
    id: int = None
    
     # Valida a figura (evitando pontos e retas)
    def incompleta(self):
        return (self.x1 == self.x2) or (self.y1 == self.y2)
    
    @property
    def x3(self):
        return (self.x2 + self.x1) / 2
    
    @property
    def y3(self):
        return self.y2
    
    # Pontos a serem usados no desenho
    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)