from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def desenhar(self, canvas, dash=()):
        pass
    
    @abstractmethod
    def incompleta(self):
        pass