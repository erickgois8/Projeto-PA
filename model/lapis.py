from figura import Figura
from dataclasses import dataclass

@dataclass
class Lapis(Figura):
    pontos: list

    def incompleta(self):
        return False