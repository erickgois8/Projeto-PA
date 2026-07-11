from model.figura import Figura
from dataclasses import dataclass

# Define lapis com base nos pontos armazenados
@dataclass
class Lapis(Figura):
    # Lista de pontos
    pontos: list

    # Cores
    borda: str
    
    # Espessura
    espessura: str

    # Verifica a figura (qualquer rabisco é válido)
    def incompleta(self):
        return False