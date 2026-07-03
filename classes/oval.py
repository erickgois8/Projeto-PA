from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Oval(Figura):
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str
    cor_preenchimento: str

    def desenhar(self, canvas, dash=()):
        canvas.create_oval(self.xi, self.yi, self.xf, self.yf,
                                   fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash)
    
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)
    
    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y