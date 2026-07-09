from dataclasses import dataclass, field
from typing import List

from model.acao import Acao

@dataclass
class HistoricoAcoes:
    dados: List[Acao] = field(default_factory=list)

    def adicionar_acao(self, acao):
        self.dados