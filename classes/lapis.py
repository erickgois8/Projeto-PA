from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Lapis(Figura):

    # Atributos de lapis
    pontos: list
    cor_borda: str
    
    def desenhar(self, canvas, dash=()):
        canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)
        return False

    def incompleta(self):
        return len(self.pontos) <= 1 # Retorna se a lista de pontos de lápis só contém um ponto (o inicial)
    
    def atualizar(self, event):
        self.pontos.append((event.x, event.y)) # Adiciona novo ponto na lista de pontos do rabisco
