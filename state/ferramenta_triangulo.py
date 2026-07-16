from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.triangulo import Triangulo
from model.figuras import Figuras
from model.estado import Estado


@dataclass
class FerramentaTriangulo(Ferramenta):
    figuras: Figuras
    estado: Estado
    triangulo_novo: Triangulo = None

    def mouse_pressionado(self, event):
        self.triangulo_novo = Triangulo(event.x, event.y, event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)
        self.ini_x = event.x
        self.ini_y = event.y

    def mouse_arrastado(self, event):
        centro = (self.ini_x + event.x) / 2

        # Vértice do triângulo isósceles
        self.triangulo_novo.x1 = centro
        
        # Base do triângulo
        self.triangulo_novo.x2 = self.ini_x
        self.triangulo_novo.x3 = event.x

        # Ajustando as ordenadas
        if event.y >= self.ini_y:
            self.triangulo_novo.y1 = self.ini_y
            self.triangulo_novo.y2 = event.y
            self.triangulo_novo.y3 = event.y

        else:
            self.triangulo_novo.y1 = event.y
            self.triangulo_novo.y2 = self.ini_y
            self.triangulo_novo.y3 = self.ini_y

        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.triangulo_novo, dash=(10,5))
    
    def mouse_solto(self, event):
        if not self.triangulo_novo.incompleta():
            self.figuras.adicionar(self.triangulo_novo)
        self.desenho.desenhar_figuras(self.figuras)