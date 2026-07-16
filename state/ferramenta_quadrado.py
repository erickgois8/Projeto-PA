from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.quadrado import Quadrado
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaQuadrdo(Ferramenta):
    figuras: Figuras
    estado: Estado
    quadrado_novo = Quadrado = None

    def mouse_pressionado(self, event):
        self.quadrado_novo = Quadrado(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        
    def mouse_arrastado(self, event):
        dx = event.x - self.quadrado_novo.x1
        dy = event.y - self.quadrado_novo.y1
        lado = max(abs(dx), abs(dy))

        x2 = self.quadrado_novo.x1 + (lado if dx >= 0 else -lado)
        y2 = self.quadrado_novo.y1 + (lado if dy >= 0 else -lado)

        self.quadrado_novo = Quadrado(self.quadrado_novo.x1, self.quadrado_novo.y1, x2, y2, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.quadrado_novo, dash=(10,5))

    def mouse_solto(self, event):
        if not self.quadrado_novo.incompleta():
            self.figuras.adicionar(self.quadrado_novo)
        self.desenho.desenhar_figuras(self.figuras)