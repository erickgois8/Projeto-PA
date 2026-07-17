from model.acao import Acao
from dataclasses import dataclasses, field

class HistoricoAcoes:
    __pilha_desfazer = list[Acao] = field(default_factory=list)
    __pilha_refazer = list[Acao] = field(default_factory=list)