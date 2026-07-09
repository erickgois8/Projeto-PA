from dataclasses import dataclass, field
from typing import List

from model.acao import Acao

# Armazena o historico em lista
@dataclass
class HistoricoAcoes:
    dados: List[Acao] = field(default_factory=list)

    def adicionar_acao(self, acao):
        self.dados