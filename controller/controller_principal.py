from controller.controller_ferramentas import ControllerFerramentas
from controller.controller_formas import ControllerFormas
from controller.controller_cores import ControllerCores
from controller.controller_modo_cor import ControllerAtalhos

from controller.desenho import Desenho, Lapis, Linha, Retangulo, Quadrado, Triangulo, Oval, Circulo
from controller.borracha import Borracha
from controller.balde_tinta import BaldeTinta

from model.ferramentas import Ferramentas
from model.figuras import Figuras
from model.cores import Cores
from model.figura_nova import FiguraNova

from view.janela import Janela

class ControllerPrincipal:
    def __init__(self, view: Janela):
        # Interface
        self.view = view

        # Gerencia as ferramentas do programa
        self.ferramentas = Ferramentas()

        # Gerencia as figuras criadas até agora
        self.figuras = Figuras()

        # Gerencia as cores selecionadas
        self.cores = Cores()

        # Inclusao das ferramentas
        self.desenho = Desenho()

        # Configura os botões da interface com suas funções
        self.controller_ferramentas = ControllerFerramentas(view, self.ferramentas)
        self.controller_formas = ControllerFormas(view, self.ferramentas)
        self.controller_cores = ControllerCores(view, self.cores)
        self.controller_atalhos = ControllerAtalhos(view, self.cores)


    # Quando o mouse é pressionado
    def iniciar_figura_nova(self, event):
        self.figura_nova = FiguraNova()

        if self.ferramentas == "lapis":
            self.figura_nova = Lapis((event.x, event.y))

        elif self.ferramentas == "linha":
            self.figura_nova == Linha(event.x, event.y, event.x, event.y)

        elif self.ferramentas == "retangulo":
            self.figura_nova = Retangulo(event.x, event.y, event.x, event.y)

        elif self.ferramentas == "quadrado":
            self.figura_nova = Retangulo(event.x, event.y, event.x, event.y)

        elif self.ferramentas == "triangulo":
            self.figura_nova = Triangulo(event.x, event.y, event.x, event.y)

        elif self.ferramentas == "oval":
            self.figura_nova = Oval(event.x, event.y, event.x, event.y)

        elif self.ferramentas == "circulo":
            self.figura_nova = Circulo(event.x, event.y, event.x, event.y)
    
    # Quando o mouse é movido
    def atualizar_figura_nova(self, event):   
        self.figura_nova.atualizar(event)

        self.desenhar_figuras()
        self.desenhar_figura_nova()
    
    # Quando o mouse é solto
    def incluir_figura_nova(self, event): 
        if not self.figura_nova.incompleta():
            self.figuras.append(self.figura_nova)

        self.desenhar_figuras()
        self.figura_nova = None
