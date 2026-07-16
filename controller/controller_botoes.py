from controller.controller_botoes_ferramentas import ControllerBotoesFerramentas
from controller.controller_botoes_formas import ControllerBotoesFormas
from controller.controller_botoes_cores import ControllerBotoesCores
from controller.controller_botoes_modo_cor import ControllerBotoesModoCor
from controller.controller_botoes_arquivos import ControllerBotoesArquivos

from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

class ControllerBotoes:
    def __init__(self, view: Janela, controller: ControllerPrincipal):
        self.controller_ferramentas = ControllerBotoesFerramentas(view, controller)
        self.controller_formas = ControllerBotoesFormas(view, controller)
        self.controller_cores = ControllerBotoesCores(view, controller)
        self.controller_modo_cor = ControllerBotoesModoCor(view, controller)
        self.controller_arquivos = ControllerBotoesArquivos(view, controller)