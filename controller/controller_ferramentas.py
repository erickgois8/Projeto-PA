from view.janela import Janela
from model.estado import Estado

class ControllerFerramentas:
    def __init__(self, view: Janela, estado: Estado):
        # Botão de lápis
        view.botoes_ferramentas.botao_lapis.configure(
            command=lambda: estado.selecionar_ferramenta("lapis"))

        # Botão de borracha
        view.botoes_ferramentas.botao_borracha.configure(
            command=lambda: estado.selecionar_ferramenta("borracha"))

        # Botão de balde de tinta
        view.botoes_ferramentas.botao_balde_tinta.configure(
            command=lambda: estado.selecionar_ferramenta("balde_tinta"))
