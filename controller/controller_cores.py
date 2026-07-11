from view.janela import Janela
from model.estado import Estado

class ControllerCores:
    def __init__(self, view: Janela, estado: Estado):

        # Botão branco
        view.botoes_cores.botao_branco.configure(
            command=lambda: estado.selecionar_cor("#FFFFFF"))

        # Botão cinza
        view.botoes_cores.botao_cinza.configure(
            command=lambda: estado.selecionar_cor("#8F8E8E"))

        # Botão preto
        view.botoes_cores.botao_preto.configure(
            command=lambda: estado.selecionar_cor("#000000"))

        # Botão vermelho
        view.botoes_cores.botao_vermelho.configure(
            command=lambda: estado.selecionar_cor("#e12729"))

        # Botão laranja
        view.botoes_cores.botao_laranja.configure(
            command=lambda: estado.selecionar_cor("#f37324"))

        # Botão amarelo
        view.botoes_cores.botao_amarelo.configure(
            command=lambda: estado.selecionar_cor("#f8cc1b"))

        # Botão verde
        view.botoes_cores.botao_verde.configure(
            command=lambda: estado.selecionar_cor("#007f4e"))

        # Botão verde claro
        view.botoes_cores.botao_verde_claro.configure(
            command=lambda: estado.selecionar_cor("#72b043"))

        # Botão ciano
        view.botoes_cores.botao_ciano.configure(
            command=lambda: estado.selecionar_cor("#53d0b5"))

        # Botão azul
        view.botoes_cores.botao_azul.configure(
            command=lambda: estado.selecionar_cor("#1982c4"))

        # Botão roxo
        view.botoes_cores.botao_roxo.configure(
            command=lambda: estado.selecionar_cor("#6a4c93"))

        # Botão rosa
        view.botoes_cores.botao_rosa.configure(
            command=lambda: estado.selecionar_cor("#f49ac2"))
        
        