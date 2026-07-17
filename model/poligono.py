from model.figura import Figura
from dataclasses import dataclass

@dataclass
class Poligono(Figura):
    # Lista de pontos
    pontos: list

    # Cores
    borda: str
    preenchimento: str
    
    # Espessura
    espessura: str

    # Verifica a figura (evitando pontos e retas)
    def incompleta(self):
        return len(self.pontos) <3