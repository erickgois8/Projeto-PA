from dataclasses import dataclass, field
from typing import List

from model.figura import Figura

# Armazena, adiciona ou apaga a figura com base na lista de dados
@dataclass
class Figuras:
    dados: List[Figura] = field(default_factory=list)

    def adicionar(self, figura):
        self.dados.append(figura)

    def remover(self, figura):
        self.dados.remove(figura)