from controller.controller_ferramentas import ControladorFerramentas
from controller.controller_formas import ControladorFormas

class ControladorPrincipal:
    def __init__(self, janela):
        self.janela = janela

        self.ferramenta_atual = None
        
        self.controlador_ferramentas = ControladorFerramentas(self)
        self.controlador_formas = ControladorFormas(self)