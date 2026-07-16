from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.oval import Oval
from model.figuras import Figuras
from model.estado import Estado


@dataclass
class FerramentaOval(Ferramenta):
    figuras: Figuras
    estado: Estado
    oval_novo: Oval = None

    def mouse_pressionado(self, event):
        self.oval_novo = Oval(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)

    def mouse_arrastado(self, event):
        self.oval_novo = Oval(self.oval_novo.x1, self.oval_novo.y1, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.oval_novo, dash=(10,5))
    
    def mouse_solto(self, event):
        if not self.oval_novo.incompleta():
            self.figuras.adicionar(self.oval_novo)
        self.desenho.desenhar_figuras(self.figuras)