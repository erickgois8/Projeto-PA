from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Retangulo(Figura):

    # Coordenadas dos pontos inicial e final, além da cor da borda e preenchimento da figura
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str
    cor_preenchimento: str

    # Pontos inicial e final para serem reutilizados
    @property
    def pontos(self):
        return (self.xi, self.yi, self.xf, self.yf)
    
    # Desenha o retângulo baseado nos pontos inicial e final
    def desenhar(self, canvas, dash=()):
        canvas.create_rectangle(self.pontos, fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash)

    # Valida a figura (verifica se os pontos inicial e final coincidem ou não)
    def incompleta(self):
        return (self.xi == self.xf) or (self.yi == self.yf)
    
    # Atualiza o ponto final
    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y