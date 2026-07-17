from model.figura import Figura
from dataclasses import dataclass, field

# Gerencia o armazenamento das figuras
@dataclass
class Figuras:
        __dados: list[Figura] = field(default_factory=list)

        def acessar(self):
            return self.__dados
        
        def adicionar(self, figura):
            self.__dados.append(figura)

        def remover(self, figura):
            self.__dados.remove(figura)

        def mover_para_frente(self, figura_selecionada):
            if figura_selecionada in self.__dados:
                indice = self.__dados.index(figura_selecionada)

                if indice < len(self.__dados) - 1:
                    self.__dados[indice], self.__dados[indice + 1] = self.__dados[indice + 1], self.__dados[indice]
                
        def mover_para_tras(self, figura_selecionada):
            if figura_selecionada in self.__dados:
                indice = self.__dados.index(figura_selecionada)

                if indice > 0:
                    self.__dados[indice], self.__dados[indice - 1] = self.__dados[indice - 1], self.__dados[indice]

        def mover_para_topo(self, figura_selecionada):
            if figura_selecionada in self.__dados:
                indice = self.__dados.index(figura_selecionada)

                figura_excluida = self.__dados.pop(indice)
                self.__dados.append(figura_excluida)

        def mover_para_fundo(self, figura_seleciondada):
            if figura_seleciondada in self.__dados:
                indice = self.__dados.index(figura_seleciondada)

                figura_excluida = self.__dados.pop(indice)
                self.__dados.insert(0, figura_excluida)