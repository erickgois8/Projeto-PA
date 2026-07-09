from dataclasses import dataclass

from model.figura import Figura

@dataclass
class FiguraNova(Figura):
    figura: Figura

    def incompleta(self):
        return self.figura.incompleta()