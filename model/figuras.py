from model.figura import Figura
from dataclasses import dataclass, field

# Gerencia o armazenamento das figuras
@dataclass
class Figuras:
    __dados: list[Figura] = field(default_factory=list)

    @property
    def acessar(self):
        return self.__dados
    
    def adicionar(self, figura):
        self.__dados.append(figura)

    def remover(self, figura):
        self.__dados.remove(figura)