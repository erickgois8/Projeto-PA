from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.circulo import Circulo
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaCirculo(Ferramenta):
    figuras: Figuras
    estado: Estado
    circulo_novo = None

    def mouse_pressionado(self, event):
        self.circulo_novo = Circulo(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)

    def mouse_arrastado(self, event):
        self.circulo_novo = Circulo(self.circulo_novo.x1, self.circulo_novo.y1, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.circulo_novo, dash=(10,5))
    
    def mouse_solto(self, event):
        if not self.circulo_novo.incompleta():
            self.figuras.adicionar(self.circulo_novo)
            self.desenho.desenhar_figuras(self.figuras)