from dataclasses import dataclass
from controller.state.ferramenta import Ferramenta
from model.retangulo import Retangulo
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaRetangulo(Ferramenta):
    figuras: Figuras
    estado: Estado
    retangulo_novo: Retangulo = None

    def mouse_pressionado(self, event):
        self.retangulo_novo = Retangulo(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        
    def mouse_arrastado(self, event):
        self.retangulo_novo = Retangulo(self.retangulo_novo.x1, self.retangulo_novo.y1, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.retangulo_novo, dash=(10,5))

    def mouse_solto(self, event):
        if not self.retangulo_novo.incompleta():
            self.figuras.adicionar(self.retangulo_novo)
        self.desenho.desenhar_figuras(self.figuras)