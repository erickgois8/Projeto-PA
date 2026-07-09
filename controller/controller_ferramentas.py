from model.ferramentas import Ferramentas
from view.janela import Janela

class ControllerFerramentas:
    def __init__(self, view: Janela, ferramentas: Ferramentas):

        # Botão de lápis
        view.frame_lateral.frame_ferramentas.botoes_ferramentas.botao_lapis.config(
            command=lambda: ferramentas.selecionar_ferramenta("lapis"))

        # Botão de borracha
        view.frame_lateral.frame_ferramentas.botoes_ferramentas.botao_borracha.config(
            command=lambda: ferramentas.selecionar_ferramenta("borracha"))

        # Botão de balde de tinta
        view.frame_lateral.frame_ferramentas.botoes_ferramentas.botao_balde_tinta.config(
            command=lambda: ferramentas.selecionar_ferramenta("balde_tinta"))
        