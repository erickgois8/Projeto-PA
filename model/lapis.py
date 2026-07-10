from model.figura import Figura
from dataclasses import dataclass

# Define lapis com base nos pontos armazenados
@dataclass
class Lapis(Figura):
    # Lista de Coordenadas
    pontos: list

    # Cores
    borda: str
    preenchimento: str
    
    # espessura
    espessura: str

    # Identifica a figura para desenho
    id: int = None

    # Valida a figura (sempre válida para o lápis)
    def incompleta(self):
        return False