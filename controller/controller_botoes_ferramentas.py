from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

class ControllerBotoesFerramentas:
    def __init__(self, view: Janela, controller: ControllerPrincipal):
        # Botão de lápis
        view.botoes_ferramentas.botao_lapis.configure(
            command=lambda: controller.selecionar_ferramenta(controller.ferramenta_lapis, "pencil"), cursor="pencil")

        # Botão de borracha
        view.botoes_ferramentas.botao_borracha.configure(
            command=lambda: controller.selecionar_ferramenta(controller.ferramenta_borracha))

        # Botão de balde de tinta
        view.botoes_ferramentas.botao_balde_tinta.configure(
            command=lambda: controller.selecionar_ferramenta(controller.ferramenta_balde_tinta, "spraycan"), cursor="spraycan")

        # Botão de seleção
        view.botoes_ferramentas.botao_selecao.configure(
            command=lambda: controller.selecionar_ferramenta(controller.ferramenta_selecao, "hand2"), cursor="hand2")