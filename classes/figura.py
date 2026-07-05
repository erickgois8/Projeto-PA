from abc import ABC, abstractmethod

class Figura(ABC):
    
    # Descreve como a figura é desenhada com base em seus atributos
    @abstractmethod
    def desenhar(self, canvas, dash=()):
        pass
    
    # Descreve como a figura se atualiza de acordo com o movimento do mouse
    @abstractmethod
    def atualizar(self, event):
        pass

    # Valida a figura
    @abstractmethod
    def incompleta(self):
        pass