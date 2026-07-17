from tkinter import *
from dataclasses import dataclass
from state.ferramenta import Ferramenta
from model.figuras import Figuras
from model.estado import Estado
import copy

@dataclass
class FerramentaSelecao(Ferramenta):
    figuras: Figuras
    estado: Estado
    canvas: Canvas

    # Figura selecionada atualmente (o programa inicia sem nenhuma figura selecionada)
    def __post_init__(self):
        self.figura_selecionada = None
        self.ini_x = None
        self.ini_y = None

    # Seleciona a figura que está sob o mouse e armazena suas coordenadas iniciais para o movimento
    def mouse_pressionado(self, event):
        self.limpar_selecao()
        raio = 3
        desenhos = self.canvas.find_overlapping(event.x - raio, event.y - raio, event.x + raio, event.y + raio)

        if desenhos:
            id_figura_selecionada = desenhos[-1]
            i = 0

            while i < len(self.figuras.acessar()) and self.figura_selecionada is None:
                if self.figuras.acessar()[i].id == id_figura_selecionada:
                    self.selecionar_figura(self.figuras.acessar()[i])
                
                i += 1
            
            self.ini_x = event.x
            self.ini_y = event.y

        else:
            self.limpar_selecao()
            return

    # Move a figura selecionada de acordo com o movimento do mouse
    def mouse_arrastado(self, event):
        if self.figura_selecionada is not None:
            self.desenho.mover_figura(self.figura_selecionada, event.x - self.ini_x, event.y - self.ini_y)
            self.desenho.desenhar_figuras(self.figuras)

            self.ini_x = event.x
            self.ini_y = event.y

        else:
            return
    
    # Finaliza a movimentação da figura selecionada e reinicia a seleção
    def mouse_solto(self, event):
        return

    # Seleciona a figura
    def selecionar_figura(self, figura):
        self.figura_selecionada = figura
        self.figura_selecionada.espessura = 4
        self.desenho.desenhar_figuras(self.figuras)

    # Reinicia a seleção da figura e as coordenadas iniciais do mouse
    def limpar_selecao(self):
        if self.figura_selecionada is not None:
            self.figura_selecionada.espessura = self.estado.espessura
            self.desenho.desenhar_figuras(self.figuras)
            
        self.figura_selecionada = None
        self.ini_x = None
        self.ini_y = None


# -------------------- OPERAÇÕES COM FIGURA SELECIONADA -------------------- #
    # Apaga a figura selecionada, se houver alguma
    def apagar_figura_selecionada(self, event):
        if self.figura_selecionada is not None:
            self.figuras.remover(self.figura_selecionada)
            self.limpar_selecao()
            self.desenho.desenhar_figuras(self.figuras)
        
        else:
            return
        
    # Copiar/colar figura selecionada
    def copiar_figura_selecionada(self, event):
        self.figuras.buffer = copy.deepcopy(self.figura_selecionada)

    def colar_figura_buffer(self, event):
        if self.figuras.buffer is not None:
            figura_copiada = copy.deepcopy(self.figuras.buffer)
            self.desenho.mover_figura(figura_copiada, 10, 10)
            figura_copiada.espessura = 2
            self.figuras.adicionar(figura_copiada)
            self.desenho.desenhar_figuras(self.figuras)

    # Move a figura selecionada para frente, se houver
    def selecionada_para_frente(self, event):
        self.figuras.mover_para_frente(self.figura_selecionada)
        self.desenho.desenhar_figuras(self.figuras)

    # Move a figura selecionada para trás, se houver
    def selecionada_para_tras(self, event):
        self.figuras.mover_para_tras(self.figura_selecionada)
        self.desenho.desenhar_figuras(self.figuras)

    # Move a figura selecionada para o topo, se houver
    def selecionada_para_topo(self, event):
        self.figuras.mover_para_topo(self.figura_selecionada)
        self.desenho.desenhar_figuras(self.figuras)

    # Move a figura selecionada para o fundo, se houver
    def selecionada_para_fundo(self, event):
        self.figuras.mover_para_fundo(self.figura_selecionada)
        self.desenho.desenhar_figuras(self.figuras)