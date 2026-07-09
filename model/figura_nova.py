from dataclasses import dataclass

from model.figura import Figura

# Define a figura com base nos dados recebidos
@dataclass
class FiguraNova(Figura):
    figura: Figura
    
# Caso a figura seja incompleta 
    def incompleta(self):
        return self.figura.incompleta()