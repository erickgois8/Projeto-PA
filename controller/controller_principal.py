from model.estado import Estado
from model.figuras import Figuras
from view.janela import Janela
from view.desenho import Desenho

from state.ferramenta_lapis import FerramentaLapis
from state.ferramenta_linha import FerramentaLinha
from state.ferramenta_retangulo import FerramentaRetangulo
from state.ferramenta_quadrado import FerramentaQuadrdo
from state.ferramenta_oval import FerramentaOval
from state.ferramenta_circulo import FerramentaCirculo
from state.ferramenta_borracha import FerramentaBorracha
from state.ferramenta_balde_tinta import FerramentaBaldeTinta
from state.ferramenta_poligono import FerramentaPoligono
from state.ferramenta_selecao import FerramentaSelecao

from controller.arquivos import Arquivos

class ControllerPrincipal:
    def __init__(self, view: Janela):
        # View (interface)
        self.view = view

        # Desenha na tela
        self.desenho = Desenho(self.view.canvas)
        
        # Controla o estado atual (ferramentas, cores e espessura)
        self.estado = Estado()

        # Armazenamento das figuras
        self.figuras = Figuras()

        # Salva e abre arquivos
        self.arquivos = Arquivos(self.figuras, self.desenho)
        
        # Configurando as ferramentas
        self.ferramenta_lapis = FerramentaLapis(self.desenho, self.figuras, self.estado)
        self.ferramenta_linha = FerramentaLinha(self.desenho, self.figuras, self.estado)
        self.ferramenta_retangulo = FerramentaRetangulo(self.desenho, self.figuras, self.estado)
        self.ferramenta_quadrado = FerramentaQuadrdo(self.desenho, self.figuras, self.estado)
        self.ferramenta_oval = FerramentaOval(self.desenho, self.figuras, self.estado)
        self.ferramenta_circulo = FerramentaCirculo(self.desenho, self.figuras, self.estado)
        self.ferramenta_poligono = FerramentaPoligono(self.desenho, self.figuras, self.estado)
        self.ferramenta_borracha = FerramentaBorracha(self.desenho, self.figuras, self.view.canvas)
        self.ferramenta_balde_tinta = FerramentaBaldeTinta(self.desenho, self.figuras, self.estado, self.view.canvas)
        self.ferramenta_selecao = FerramentaSelecao(self.desenho, self.figura)

        # Ferramenta atual
        self.ferramenta_atual = self.ferramenta_lapis

        # Responde aos eventos de mouse
        self.view.canvas.bind('<ButtonPress-1>', self.mouse_pressionado)
        self.view.canvas.bind('<B1-Motion>', self.mouse_arrastado)
        self.view.canvas.bind('<ButtonRelease-1>', self.mouse_solto)
        self.view.canvas.bind('<ButtonPress-3>', self.mouse_finalizado)

    # Para mudar de ferramenta        
    def selecionar_ferramenta(self, ferramenta):
        self.ferramenta_atual = ferramenta

    # Usa a ferramenta a partir dos eventos de mouse
    def mouse_pressionado(self, event):
        self.ferramenta_atual.mouse_pressionado(event)

    def mouse_arrastado(self, event):
        self.ferramenta_atual.mouse_arrastado(event)

    def mouse_solto(self, event):
        self.ferramenta_atual.mouse_solto(event)

    def mouse_finalizado(self, event):
        self.ferramenta_atual.finalizar(event)