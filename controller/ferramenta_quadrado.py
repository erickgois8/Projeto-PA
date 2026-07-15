from dataclasses import dataclass
from controller.ferramenta import Ferramenta
from model.quadrado import Quadrado
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaQuadrado(Ferramenta):
    figuras: Figuras
    estado: Estado
    quadrado_novo= None

    def mouse_pressionado(self, event):
        self.quadrado_novo= Quadrado(event.x, event.y, event.x, event.y,self.estado.cor_borda,
                                        self.estado.espessura, self.estado.__cor_preenchimento)
        
    def mouse_arrastado(self, event):
        self.quadrado_novo= Quadrado(self.linha_nova.x1, self.linha_nova.y1, event.x, event.y, self.estado.cor_borda,
                                       self.estado.espessura, self.estado.cor_preenchimento, dash=(10, 5))
         
        if isinstance(self.quadrado_novo, Quadrado):
            dx = event.x - self.quadrado_novo.x1
            dy = event.y - self.quadrado_novo.y1

            lado = max(abs(dx), abs(dy))
    
    def mouse_solto(self, event):
        if not self.quadrado_novo.incompleta():
            self.figuras.adicionar(self.quadrado_novo)
            self.desenho.desenhar_figuras(self.figuras)