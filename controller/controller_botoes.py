from controller.controller_ferramentas import ControllerFerramentas
from controller.controller_formas import ControllerFormas
from controller.controller_cores import ControllerCores
from controller.controller_modo_cor import ControllerModoCor
from controller.controller_arquivos import ControllerArquivos

from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

class ControllerBotoes:
    def __init__(self, view: Janela, controller: ControllerPrincipal):
        self.controller_ferramentas = ControllerFerramentas(view, controller)
        self.controller_formas = ControllerFormas(view, controller)
        self.controller_cores = ControllerCores(view, controller)
        self.controller_modo_cor = ControllerModoCor(view, controller)
        self.controller_arquivos = ControllerArquivos(view, controller)