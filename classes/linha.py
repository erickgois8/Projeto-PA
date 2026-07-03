from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Linha(Figura):

    # Atributos básicos para desenhar uma linha
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str

    @property
    def pontos(self):
        return (self.xi, self.yi, self.xf, self.yf) # Pontos inicial e final para serem reutilizados
    
    def desenhar(self, canvas, dash=()):
        canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)

    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf) # Retorna se o ponto final coincide ou não com o inicial

    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y