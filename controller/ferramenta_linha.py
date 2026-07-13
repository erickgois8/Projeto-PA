from dataclasses import dataclass
from controller.ferramenta import Ferramenta
from model.linha import Linha
from model.figuras import Figuras


@dataclass
class FerramentaLinha(Ferramenta):
    figuras: Figuras
    linha_nova: Linha = None

    def mouse_pressionado(self, event):
        self.linha_nova = Linha ([(event.x, event.y)])

    def mouse_arrastado(self, event):
        self.linha_nova.pontos.append((event.x, event.y))
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.linha_nova, dash =(10,5))
    
    def mouse_solto(self, event):
        if not self.linha_nova.incompleta():
            self.figuras.adicionar(self.linha_nova)
            self.desenho.desenhar_figuras(self.figuras)


    self.estado.cor_borda
    self.estado.espessura