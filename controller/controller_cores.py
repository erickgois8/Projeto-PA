from model.cores import Cores
from view.janela import Janela

class ControllerCores:
    def __init__(self, view: Janela, cores: Cores):

        # Botão branco
        view.frame_lateral.frame_cores.botoes_cores.botao_branco.config(
            command=lambda: cores.selecionar_cor("branco", cores.modo))

        # Botão cinza
        view.frame_lateral.frame_cores.botoes_cores.botao_cinza.config(
            command=lambda: cores.selecionar_cor("cinza", cores.modo))

        # Botão preto
        view.frame_lateral.frame_cores.botoes_cores.botao_preto.config(
            command=lambda: cores.selecionar_cor("preto", cores.modo))

        # Botão vermelho
        view.frame_lateral.frame_cores.botoes_cores.botao_vermelho.config(
            command=lambda: cores.selecionar_cor("vermelho", cores.modo))

        # Botão laranja
        view.frame_lateral.frame_cores.botoes_cores.botao_laranja.config(
            command=lambda: cores.selecionar_cor("laranja", cores.modo))

        # Botão amarelo
        view.frame_lateral.frame_cores.botoes_cores.botao_amarelo.config(
            command=lambda: cores.selecionar_cor("amarelo", cores.modo))

        # Botão verde
        view.frame_lateral.frame_cores.botoes_cores.botao_verde.config(
            command=lambda: cores.selecionar_cor("verde", cores.modo))

        # Botão verde claro
        view.frame_lateral.frame_cores.botoes_cores.botao_verde_claro.config(
            command=lambda: cores.selecionar_cor("verde_claro", cores.modo))

        # Botão ciano
        view.frame_lateral.frame_cores.botoes_cores.botao_ciano.config(
            command=lambda: cores.selecionar_cor("ciano", cores.modo))

        # Botão azul
        view.frame_lateral.frame_cores.botoes_cores.botao_azul.config(
            command=lambda: cores.selecionar_cor("azul", cores.modo))

        # Botão roxo
        view.frame_lateral.frame_cores.botoes_cores.botao_roxo.config(
            command=lambda: cores.selecionar_cor("roxo", cores.modo))

        # Botão rosa
        view.frame_lateral.frame_cores.botoes_cores.botao_rosa.config(
            command=lambda: cores.selecionar_cor("rosa", cores.modo))