from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Lapis(Figura):

    # Lista dos pontos por onde o mouse passa, além da cor da borda da figura
    pontos: list
    cor_borda: str
    
    # Desenha um rabisco de lápis unindo todos os pontos armazenados
    def desenhar(self, canvas, dash=()):
        self.tipo = "lapis"
        self.id = canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash, width=3)
        return False

    def redesenhar(self, canvas, cor):
        self.id = canvas.create_line(self.pontos, fill=self.cor_borda, width=3)
        
    # Valida a figura (qualquer rabisco é válido)
    def incompleta(self):
        return False
    
    # Adiciona na lista o novo ponto em que mouse passa
    def atualizar(self, event):
        self.pontos.append((event.x, event.y))