from controller.controller_ferramentas import ControllerFerramentas
from controller.controller_formas import ControllerFormas
from controller.controller_cores import ControllerCores
from controller.controller_modo_cor import ControllerModoCor

from controller.desenho import Desenho
from controller.desenho_figura_nova import DesenhoFiguraNova
from controller.borracha import Borracha
from controller.balde_tinta import BaldeTinta

from model.ferramentas import Ferramentas
from model.figuras import Figuras
from model.cores import Cores

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

        # Desenha no canvas
        self.desenho = Desenho(self.view.canvas)

        # Inclusão das ferramentas de desenho da nova figura
        self.desenho_figura_nova = DesenhoFiguraNova(self.desenho, 
                                                     self.ferramentas.tipo_ferramenta,
                                                     self.cores.borda,
                                                     self.cores.preenchimento)
        
        # Inclusão da ferramenta de borracha
        self.borracha = Borracha(self.desenho)

        # Inclusão da ferramenta de balde de tinta
        self.balde_tinta = BaldeTinta(self.desenho)

        # Configura os botões da interface com suas funções
        self.controller_ferramentas = ControllerFerramentas(view, self.ferramentas)
        self.controller_formas = ControllerFormas(view, self.ferramentas)
        self.controller_cores = ControllerCores(view, self.cores)
        self.controller_modo_cor = ControllerModoCor(view, self.cores)

        # Configura o clique do mouse na area de desenho
        self.view.canvas.bind('<ButtonPress-1>', self.usar_ferramenta)


    # Método geral para usar as ferramentas
    def usar_ferramenta(self, event):
        self.view.canvas.unbind('<B1-Motion>')
        self.view.canvas.unbind('<ButtonRelease-1>')
         
        if self.ferramentas.tipo_ferramenta == "borracha":
            self.borracha.apagar(event, self.view.canvas, self.figuras)
            self.view.canvas.bind('<B1-Motion>', lambda event: self.borracha.apagar(event, self.view.canvas, self.figuras))

        elif self.ferramentas.tipo_ferramenta == "balde_tinta":
            self.balde_tinta.preencher(event, self.view.canvas, self.figuras, self.cores.preenchimento)

        else:
            # Atualiza os dados da nova figura
            self.desenho_figura_nova.tipo = self.ferramentas.tipo_ferramenta
            self.desenho_figura_nova.borda = self.cores.borda
            self.desenho_figura_nova.preenchimento = self.cores.borda

            # Cria e deseneha a nova figura
            self.desenho_figura_nova.iniciar(event)
            self.view.canvas.bind('<B1-Motion>', lambda event: self.desenho_figura_nova.atualizar(event, self.view.canvas, self.figuras))
            self.view.canvas.bind('<ButtonRelease-1>', lambda event: self.desenho_figura_nova.incluir(event, self.view.canvas,self.figuras))