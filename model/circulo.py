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
    
    # Espessura
    espessura: str

    # Calcula o raio do círculo
    @property
    def raio(self):
        return ((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) ** 0.5
    
    # Verifica a figura (evitando pontos)
    def incompleta(self):
        return (self.x1 == self.x2) and (self.y1 == self.y2)