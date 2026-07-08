from controller.config_btn_ferramentas import ConfigFerramentas


class ControladorFerramentas:
    def __init__(self, controlador_principal):
        self.controlador = controlador_principal
        self.janela = controlador_principal.janela

        self.config_ferramentas = ConfigFerramentas(self)

    def selecionar_ferramenta(self, ferramenta):
        self.controlador.ferramenta_atual = ferramenta
        print("Ferramenta atual:", ferramenta)  # tirar dps