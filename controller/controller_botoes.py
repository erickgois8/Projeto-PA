from controller.controller_ferramentas import ControllerFerramentas
from controller.controller_formas import ControllerFormas
from controller.controller_cores import ControllerCores
from controller.controller_modo_cor import ControllerModoCor

from view.janela import Janela
from model.estado import Estado

class ControllerBotoes:
    def __init__(self, view: Janela, estado: Estado):
        self.controller_ferramentas = ControllerFerramentas(view, estado)
        self.controller_formas = ControllerFormas(view, estado)
        self.controller_cores = ControllerCores(view, estado)
        self.controller_modo_cor = ControllerModoCor(view, estado)