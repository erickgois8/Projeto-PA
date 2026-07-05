from classes.figura import Figura
from dataclasses import dataclass, field

@dataclass
class Circulo(Figura):
    
    # Coordenadas dos pontos inicial e final, além da cor da borda e de preenchimento da figura
    xi: int
    yi: int
    xf: int
    yf: int
    cor_borda: str
    cor_preenchimento: str

    # Desenha o circulo baseado nos pontos inicial e final
    def desenhar(self, canvas, dash=()):
        self.tipo = "circulo"

        # Cálculo do raio (por Pitágoras)
        self.raio = ((self.yf - self.yi) ** 2 + (self.xf - self.xi) ** 2) ** 0.5

        # Oval limitada em um quadrado (circulo)
        self.id = canvas.create_oval(self.xi - self.raio, self.yi - self.raio, self.xi + self.raio, self.yi + self.raio,
                            fill=self.cor_preenchimento, outline=self.cor_borda, dash=dash, width=3)
        
    def redesenhar(self, canvas, cor):
            self.cor_preenchimento = cor
            self.id = canvas.create_oval(self.xi - self.raio, self.yi - self.raio, self.xi + self.raio, self.yi + self.raio,
                            fill=self.cor_preenchimento, outline=self.cor_borda, width=3)
            
    # Valida a figura (se o ponto inicial coincide ou não com o final)
    def incompleta(self):
        return (self.xi, self.yi) == (self.xf, self.yf)
  
    # Atualiza o ponto final pelo movimento do mouse
    def atualizar(self, event):
        self.xf = event.x
        self.yf = event.y