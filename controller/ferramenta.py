from dataclasses import dataclass
from abc import ABC, abstractmethod

from view.janela import Janela
from view.desenho import Desenho

@dataclass
class Ferramenta(ABC):
    view: Janela
    desenho: Desenho

    def __post_init__(self):
        self.canvas = self.view.canvas

    @abstractmethod
    def mouse_pressionado(self, event):
        pass

    def mouse_arrastado(self, event):
        pass

    def mouse_solto(self, event):
        pass