from abc import ABC, abstractmethod

class Acao(ABC):
    
    @abstractmethod
    def executar(self):
        pass

    @abstractmethod
    def desfazer(self):
        pass