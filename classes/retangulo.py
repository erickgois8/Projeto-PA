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

    # Desenha o retângulo baseado nos pontos inicial e final
    def desenhar(self, canvas, dash=()):
        self.tipo = "retangulo"
        self.id = canvas.create_rectangle(self.xi, self.yi, self.xf, self.yf, fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash, width=3)

    # Atualiza o ponto final
    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y

    # Valida a figura (verifica se os pontos inicial e final coincidem ou não)
    def incompleta(self):
        return (self.xi == self.xf) or (self.yi == self.yf)