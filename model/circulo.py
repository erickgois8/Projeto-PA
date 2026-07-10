from model.figura import Figura
from dataclasses import dataclass


# Define um Circulo (centro e ponto qualquer)
@dataclass
class Circulo(Figura):
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

    # Valida a figura (se os pontos inicial e final coincidem ou não)
    def incompleta(self):
        return (self.x1 == self.x2) and (self.y1 == self.y2)
    
    # Raio do círculo
    @property
    def raio(self):
        return ((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) ** 0.5
    
    # Pontos a serem usados no desenho
    @property
    def pontos(self):
        return (self.x1 - self.raio, self.y1 - self.raio, self.x2 + self.raio, self.y2 + self.raio)