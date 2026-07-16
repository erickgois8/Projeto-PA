from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.linha import Linha
from model.figuras import Figuras
from model.estado import Estado


@dataclass
class FerramentaLinha(Ferramenta):
    figuras: Figuras
    estado: Estado
    linha_nova: Linha = None

    def mouse_pressionado(self, event):
        self.linha_nova = Linha(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.espessura)

    def mouse_arrastado(self, event):
        self.linha_nova = Linha(self.linha_nova.x1, self.linha_nova.y1, event.x, event.y, self.estado.cor_borda, self.estado.espessura)
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.linha_nova, dash=(10,5))
    
    def mouse_solto(self, event):
        if not self.linha_nova.incompleta():
            self.figuras.adicionar(self.linha_nova)
        self.desenho.desenhar_figuras(self.figuras)