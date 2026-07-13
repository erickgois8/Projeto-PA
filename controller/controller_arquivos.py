from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

class ControllerArquivos:
    def __init__(self, view: Janela, controller: ControllerPrincipal):
        view.botoes_salvar.botao_abrir.configure(command=lambda: controller.arquivos.abrir())
        
        view.botoes_salvar.botao_salvar.configure(command=controller.arquivos.salvar)