from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Circulo(Figura):
    
    # Atributos básicos para desenho do círculo
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str
    cor_preenchimento: str

    def desenhar(self, canvas, dash=()):
        self.raio = ((self.yf - self.yi) ** 2 + (self.xf - self.xi) ** 2) ** 0.5                                 # Cálculo do raio (por Pitágoras)
        canvas.create_oval(self.xi - self.raio, self.yi - self.raio, self.xi + self.raio, self.yi + self.raio,   # Oval limitada em um quadrado (círculo)
                            fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash)
        
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf) # Retorna se o ponto final coincide ou não com o inicial
  

    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y