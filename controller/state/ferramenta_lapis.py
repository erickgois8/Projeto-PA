from dataclasses import dataclass
from controller.state.ferramenta import Ferramenta
from model.lapis import Lapis
from model.figuras import Figuras
from model.estado import Estado

@dataclass
class FerramentaLapis(Ferramenta):
    figuras: Figuras
    estado: Estado
    lapis_novo: Lapis = None

    def mouse_pressionado(self, event):
        self.lapis_novo = Lapis([(event.x, event.y)], self.estado.cor_borda, self.estado.espessura)

    def mouse_arrastado(self, event):
        self.lapis_novo.pontos.append((event.x, event.y))
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.lapis_novo, dash=(10, 5))

    def mouse_solto(self, event):
        if len(self.lapis_novo.pontos) == 1:
            self.lapis_novo.pontos.append(self.lapis_novo.pontos[0])
        self.figuras.adicionar(self.lapis_novo)
        self.desenho.desenhar_figuras(self.figuras)