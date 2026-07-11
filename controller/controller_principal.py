from controller.controller_ferramentas import ControllerFerramentas
from controller.controller_formas import ControllerFormas
from controller.controller_cores import ControllerCores
from controller.controller_modo_cor import ControllerModoCor

from model.estado import Estado
from model.figuras import Figuras
from model.figura import Figura
from model.lapis import Lapis
from model.linha import Linha
from model.retangulo import Retangulo
from model.quadrado import Quadrado
from model.oval import Oval
from model.circulo import Circulo

from view.janela import Janela
from view.desenho import Desenho

class ControllerPrincipal:
    def __init__(self, view: Janela):
        # Interface
        self.view = view

        # Área de desenho
        canvas = self.view.canvas
        
        # Controla o estado atual (ferramentas, cores, espessura)
        self.estado = Estado()

        # Configura os botões da interface com suas funções
        self.controller_ferramentas = ControllerFerramentas(self.view, self.estado)
        self.controller_formas = ControllerFormas(self.view, self.estado)
        self.controller_cores = ControllerCores(self.view, self.estado)
        self.controller_modo_cor = ControllerModoCor(self.view, self.estado)

        # Ferramenta que desenha na tela
        self.desenho = Desenho(canvas)

        # Armazenamento das figuras
        self.figuras = Figuras()

        # Figura nova a ser criada
        self.figura_nova = None

        # Responde aos eventos de mouse
        canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)
        
    # QUANDO O MOUSE É PRESSIONADO -> inicia a figura correspondente à ferramenta atual
    def iniciar_figura_nova(self, event):
        # LAPIS
        if self.estado.ferramenta_atual == "lapis":
            self.figura_nova = Lapis([(event.x, event.y)], self.estado.cor_borda, self.estado.espessura)

        # LINHA
        elif self.estado.ferramenta_atual == "linha":
            self.figura_nova = Linha(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.espessura)

        # RETANGULO
        elif self.estado.ferramenta_atual == "retangulo":
            self.figura_nova = Retangulo(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)

        # QUADRADO
        elif self.estado.ferramenta_atual == "quadrado":
            self.figura_nova = Quadrado(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)  

        # OVAL
        elif self.estado.ferramenta_atual == "oval":
            self.figura_nova = Oval(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)

        # CIRCULO
        elif self.estado.ferramenta_atual == "circulo":
            self.figura_nova = Circulo(event.x, event.y, event.x, event.y, self.estado.cor_borda, self.estado.cor_preenchimento, self.estado.espessura)

    # QUANDO O MOUSE É ARRASTADO -> atualização da figura na tela
    def atualizar_figura_nova(self, event):
        # LAPIS
        if isinstance(self.figura_nova, Lapis):
            self.figura_nova.pontos.append((event.x, event.y))

        # LINHA
        elif isinstance(self.figura_nova, Linha):
            self.figura_nova.x2, self.figura_nova.y2 = event.x, event.y

        # RETANGULO
        elif isinstance(self.figura_nova, Retangulo):
            self.figura_nova.x2, self.figura_nova.y2 = event.x, event.y

        # QUADRADO
        elif isinstance(self.figura_nova, Quadrado):
            dx = event.x - self.figura_nova.x1
            dy = event.y - self.figura_nova.y1

            lado = max(abs(dx), abs(dy))

            self.figura_nova.x2 = self.figura_nova.x1 + (lado if dx >= 0 else -lado)
            self.figura_nova.y2 = self.figura_nova.y1 + (lado if dy >= 0 else -lado)

        # OVAL
        elif isinstance(self.figura_nova, Oval):
            self.figura_nova.x2, self.figura_nova.y2 = event.x, event.y

        # CIRCULO
        elif isinstance(self.figura_nova, Circulo):
            self.figura_nova.x2, self.figura_nova.y2 = event.x, event.y

        # ATUALIZA A TELA
        self.desenho.desenhar_figuras(self.figuras)
        self.desenho.desenhar_figura(self.figura_nova, dash=(10,5))

    # QUANDO O MOUSE É SOLTO -> a figura é incluída na lista de figuras, caso esteja completa
    def incluir_figura_nova(self, event):
        if self.figura_nova is None:
            return
        
        if not self.figura_nova.incompleta():
            self.figuras.adicionar(self.figura_nova)

        self.desenho.desenhar_figuras(self.figuras)
        self.figura_nova = None