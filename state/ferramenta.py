from dataclasses import dataclass
from abc import ABC, abstractmethod

from view.desenho import Desenho

@dataclass
class Ferramenta(ABC):
    desenho: Desenho

    @abstractmethod
    def mouse_pressionado(self, event):
        pass

    def mouse_arrastado(self, event):
        pass

    def mouse_solto(self, event):
        pass

    def finalizar(self, event):
        pass