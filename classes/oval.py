from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Oval(Figura):

    # Atributos básicos para a criação do oval
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str
    cor_preenchimento: str

    def desenhar(self, canvas, dash=()):
        canvas.create_oval(self.xi, self.yi, self.xf, self.yf,                                       # Define os limites do oval
                                   fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash)
    
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf) # Retorna se o ponto final coincide ou não com o inicial
    
    def atualizar(self, event):    # Atualiza o ponto final conforme o mouse é movido
        self.xf = event.x
        self.yf = event.y