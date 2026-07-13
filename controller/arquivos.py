from dataclasses import dataclass
import pickle
from model.figuras import Figuras
from view.desenho import Desenho

@dataclass
class Arquivos:
    figuras: Figuras

    desenho: Desenho

    def salvar(self):
        with open("paint.pkl", "wb") as arquivo:
            pickle.dump(self.figuras.acessar, arquivo)

    def abrir(self):
        with open("paint.pkl", "rb") as arquivo:
            figuras = pickle.load(arquivo)
            self.desenho.desenhar_figuras(figuras)