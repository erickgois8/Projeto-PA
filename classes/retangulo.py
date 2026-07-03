from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Retangulo(Figura):

    # Atributos básicos para criação do retângulo
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str
    cor_preenchimento: str

    @property
    def pontos(self):
        return (self.xi, self.yi, self.xf, self.yf) # Pontos inicial e final para serem reutilizados
    
    def desenhar(self, canvas, dash=()):
        canvas.create_rectangle(self.pontos, fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash)

    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf) # Retorna se o ponto final coincide ou não com o inicial
    
    def atualizar(self, event): # Atualiza apenas o ponto final conforme o mouse é movido
        self.xf = event.x
        self.yf = event.y