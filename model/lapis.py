from figura import Figura
from dataclasses import dataclass
# Define lapis com base nos dados
@dataclass
class Lapis(Figura):
    pontos: list

    def incompleta(self):
        return False