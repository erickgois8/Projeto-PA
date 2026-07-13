from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

class ControllerArquivos:
    def __init__(self, view: Janela, controller: ControllerPrincipal):
        view.botoes_salvar.botao_salvar.configure(command=controller.arquivos.salvar)
        
        view.botoes_salvar.botao_abrir.configure(command=controller.arquivos.abrir)