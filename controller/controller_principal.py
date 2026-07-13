from model.estado import Estado
from model.figuras import Figuras
from view.janela import Janela
from view.desenho import Desenho

from controller.controller_botoes import ControllerBotoes
from controller.ferramenta_lapis import FerramentaLapis
from controller.ferramenta_linha import FerramentaLinha
from controller.ferramenta_retangulo import FerramentaRetangulo
from controller.ferramenta_quadrado import FerramentaQuadrdo
from controller.ferramenta_oval import FerramentaOval
from controller.ferramenta_circulo import FerramentaCirculo

class ControllerPrincipal:
    def __init__(self, view: Janela):
        # View (interface)
        self.view = view

        # Área de desenho
        self.canvas = self.view.canvas

        # Desenha na tela
        self.desenho = Desenho(self.canvas)
        
        # Controla o estado atual (ferramentas, cores e espessura)
        self.estado = Estado()

        # Configura os botões da interface
        self.controller_botoes = ControllerBotoes(self.view, self.estado)

        # Armazenamento das figuras
        self.figuras = Figuras()
        
        # Configurando as ferramentas
        self.ferramenta_lapis = FerramentaLapis(self.view, self.desenho, self.figuras, self.estado)
        self.ferramenta_linha = FerramentaLinha(self.view, self.desenho, self.figuras, self.estado)
        self.ferramenta_retangulo = FerramentaRetangulo(self.view, self.desenho, self.figuras, self.estado)
        self.ferramenta_quadrado = FerramentaQuadrdo(self.view, self.desenho, self.figuras, self.estado)
        self.ferramenta_oval = FerramentaOval(self.view, self.desenho, self.figuras, self.estado)
        self.ferramenta_circulo = FerramentaCirculo(self.view, self.desenho, self.figuras, self.estado)

        # Ferramenta atual
        self.ferramenta_atual = self.ferramenta_lapis

        # Responde aos eventos de mouse
        self.canvas.bind('<ButtonPress-1>', self.mouse_pressionado)
        self.canvas.bind('<B1-Motion>', self.mouse_arrastado)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_solto)

    # Para mudar de ferramenta        
    def mudar_ferramenta(self):
        if self.estado.ferramenta_escolhida == "lapis":
            self.ferramenta_atual = self.ferramenta_lapis

        elif self.estado.ferramenta_escolhida == "linha":
            self.ferramenta_atual = self.ferramenta_linha

        elif self.estado.ferramenta_escolhida == "retangulo":
            self.ferramenta_atual = self.ferramenta_retangulo

        elif self.estado.ferramenta_escolhida == "quadrado":
            self.ferramenta_atual = self.ferramenta_quadrado

        elif self.estado.ferramenta_escolhida == "oval":
            self.ferramenta_atual = self.ferramenta_oval

        elif self.estado.ferramenta_escolhida == "quadrado":
            self.ferramenta_atual = self.ferramenta_quadrado

    # Usa a ferramenta a partir dos eventos de mouse
    def mouse_pressionado(self, event):
        self.ferramenta_atual.mouse_pressionado(event)

    def mouse_arrastado(self, event):
        self.ferramenta_atual.mouse_arrastado(event)

    def mouse_solto(self, event):
        self.ferramenta_atual.mouse_solto(event)