from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Linha(Figura):

    # Coordenadas dos pontos inicial e final, além da cor da borda da figura
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str

    # Desenha uma linha baseado nos pontos inicial e final
    def desenhar(self, canvas, dash=()):
        self.tipo = "linha"
        self.id = canvas.create_line(self.xi, self.yi, self.xf, self.yf, fill=self.cor_borda, dash=dash, width=3)

    # Atualiza o ponto final
    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y

    # Valida a figura (se o ponto final coincide ou não com o inicial)
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)