from dataclasses import dataclass
from controller.state.ferramenta import Ferramenta
from model.poligono import Poligono
from model.figuras import Figuras
from model.estado import Estado


@dataclass
class FerramentaPoligono(Ferramenta):
    figuras: Figuras
    estado: Estado
    poligono_novo: Poligono = None

    def mouse_pressionado(self, event):
        if self.poligono_novo is None:
            self.poligono_novo = Poligono([(event.x, event.y)], self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        else:
            self.poligono_novo.pontos.append((event.x, event.y))

    def mouse_arrastado(self, event):
        if self.poligono_novo is None:
            return
        
        pontos_previa = self.poligono_novo.pontos + [(event.x, event.y)]
        self.desenho.desenhar_figuras(self.figuras)

        if len(pontos_previa) >=3:
            previa = Poligono(pontos_previa, self.poligono_novo.borda, self.poligono_novo.preenchimento, self.poligono_novo.espessura)
            self.desenho.desenhar_figura(previa, dash = (10,5))

    # Os vértices são definidos por cliques; soltar o botão não finaliza a figura.
    def mouse_solto(self, event):
        pass

    def finalizar(self, event):
        if self.poligono_novo is not None and not self.poligono_novo.incompleta():
            self.figuras.adicionar(self.poligono_novo)

        self.poligono_novo = None
        self.desenho.desenhar_figuras(self.figuras)
