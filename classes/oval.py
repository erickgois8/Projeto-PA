from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Oval(Figura):

    # Coordenadas dos pontos inicial e final, bem como cor da borda e preenchimento da figura
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str
    cor_preenchimento: str

    # Desenha a oval baseada nos pontos inicial e final (que limitam um retângulo)
    def desenhar(self, canvas, dash=()):
        self.tipo = "oval"
        self.id = canvas.create_oval(self.xi, self.yi, self.xf, self.yf, fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash, width=3)
        
    # Atualiza o ponto final
    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y

    # Valida a figura (se a elipse forma uma linha horizontal ou vertical ou se os pontos inicial e final coincidem)
    def incompleta(self):
        return (self.xi == self.xf or self.yi == self.yf)
    ,