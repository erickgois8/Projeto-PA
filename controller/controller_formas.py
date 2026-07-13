from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

class ControllerFormas:
     def __init__(self, view: Janela, controller: ControllerPrincipal):
        # Botão linha
        view.botoes_formas.botao_linha.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_linha))

        # Botão círculo
        view.botoes_formas.botao_circulo.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_circulo))

        # Botão oval
        view.botoes_formas.botao_oval.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_oval))
        
        # Botão quadrado
        view.botoes_formas.botao_quadrado.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_quadrado))
        
        # Botão retangulo
        view.botoes_formas.botao_retangulo.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_retangulo))