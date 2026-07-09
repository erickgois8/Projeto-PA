from dataclasses import dataclass, field
from typing import List

from model.figura import Figura

@dataclass
class Figuras:
    dados: List[Figura] = field(default_factory=list)

    def adicionar_figura(self, figura):
        self.dados.append(figura)

    def apagar_figura(self, figura):
        self.dados.remove(figura)