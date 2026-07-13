from dataclasses import dataclass
from controller.ferramenta import Ferramenta
from model.retangulo import Retangulo
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaRetangulo(Ferramenta):
    figuras: Figuras
    estado: Estado
    retangulo_novo= None

    def mouse_pressionado(self, event):
        self.retangulo_novo= Retangulo(event.x, event.y, event.x, event.y,self.estado.cor_borda,
                                        self.estado.espessura, self.estado.__cor_preenchimento)
        
    def mouse_arrastado(self, event):
        self.retangulo_novo= Retangulo(self.linha_nova.x1, self.linha_nova.y1, event.x, event.y, self.estado.cor_borda,
                                       self.estado.espessura, self.estado.cor_preenchimento, dash=(10, 5))
    
    def mouse_solto(self, event):
        if not self.retangulo_novo.incompleta():
            self.figuras.adicionar(self.retangulo_novo)
            self.desenho.desenhar_figuras(self.figuras)