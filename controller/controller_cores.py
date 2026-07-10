from model.cores import Cores
from view.janela import Janela

class ControllerCores:
    def __init__(self, view: Janela, cores: Cores):

        botoes_cores = view.frame_lateral.frame_cores.botoes_formas

        # Botão branco
        botoes_cores.botao_branco.config(
            command=lambda: cores.selecionar_cor("branco"))

        # Botão cinza
        botoes_cores.botao_cinza.config(
            command=lambda: cores.selecionar_cor("cinza"))

        # Botão preto
        botoes_cores.botao_preto.config(
            command=lambda: cores.selecionar_cor("preto"))

        # Botão vermelho
        botoes_cores.botao_vermelho.config(
            command=lambda: cores.selecionar_cor("vermelho"))

        # Botão laranja
        botoes_cores.botao_laranja.config(
            command=lambda: cores.selecionar_cor("laranja"))

        # Botão amarelo
        botoes_cores.botao_amarelo.config(
            command=lambda: cores.selecionar_cor("amarelo"))

        # Botão verde
        botoes_cores.botao_verde.config(
            command=lambda: cores.selecionar_cor("verde"))

        # Botão verde claro
        botoes_cores.botao_verde_claro.config(
            command=lambda: cores.selecionar_cor("verde_claro"))

        # Botão ciano
        botoes_cores.botao_ciano.config(
            command=lambda: cores.selecionar_cor("ciano"))

        # Botão azul
        botoes_cores.botao_azul.config(
            command=lambda: cores.selecionar_cor("azul"))

        # Botão roxo
        botoes_cores.botao_roxo.config(
            command=lambda: cores.selecionar_cor("roxo"))

        # Botão rosa
        botoes_cores.botao_rosa.config(
            command=lambda: cores.selecionar_cor("rosa"))