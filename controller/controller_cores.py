from view.janela import Janela
from model.estado import Estado
from tkinter import *

class ControllerCores:
    def __init__(self, view: Janela, estado: Estado):
        #Imagens botão sem preenchimento
        self.img_botao_sem_preenchimento_ativo = PhotoImage(file="images/sem_preenchimento_ativo.png")
        self.img_botao_sem_preenchimento = PhotoImage(file="images/sem_preenchimento.png")

        # Botão branco
        view.botoes_cores.botao_branco.configure(
            command=lambda: self.trocar_cor(estado, view, "#FFFFFF"))

        # Botão cinza
        view.botoes_cores.botao_cinza.configure(
            command=lambda: self.trocar_cor(estado, view, "#8F8E8E"))

        # Botão preto
        view.botoes_cores.botao_preto.configure(
            command=lambda: self.trocar_cor(estado, view, "#000000"))

        # Botão vermelho
        view.botoes_cores.botao_vermelho.configure(
            command=lambda: self.trocar_cor(estado, view, "#e12729"))

        # Botão laranja
        view.botoes_cores.botao_laranja.configure(
            command=lambda: self.trocar_cor(estado, view, "#f37324"))

        # Botão amarelo
        view.botoes_cores.botao_amarelo.configure(
            command=lambda: self.trocar_cor(estado, view, "#f8cc1b"))

        # Botão verde
        view.botoes_cores.botao_verde.configure(
            command=lambda: self.trocar_cor(estado, view, "#007f4e"))

        # Botão verde claro
        view.botoes_cores.botao_verde_claro.configure(
            command=lambda: self.trocar_cor(estado, view, "#72b043"))

        # Botão ciano
        view.botoes_cores.botao_ciano.configure(
            command=lambda: self.trocar_cor(estado, view, "#53d0b5"))

        # Botão azul
        view.botoes_cores.botao_azul.configure(
            command=lambda: self.trocar_cor(estado, view, "#1982c4"))

        # Botão roxo
        view.botoes_cores.botao_roxo.configure(
            command=lambda: self.trocar_cor(estado, view, "#6a4c93"))

        # Botão rosa
        view.botoes_cores.botao_rosa.configure(
            command=lambda: self.trocar_cor(estado, view, "#f49ac2"))
        
    # Junta as funções de atualizar botão de cor de borda e de preenchimento
    def trocar_cor(self, estado: Estado, view, cor):
        if estado.modo_cor == "borda":
            estado.selecionar_cor = cor
            self.atualiza_botao_borda(estado, view)

        elif estado.modo_cor == "preenchimento":
            estado.selecionar_cor = cor
        
        self.atualiza_botao_sem_preenchimento(estado, view)
        self.atualiza_botao_preenchimento(estado, view)

        
    # Atualiza o botão de sem preenchimento para que fique ativo quando selecionado e inativo quando não
    def atualiza_botao_sem_preenchimento(self, estado, view):
        if estado.cor_preenchimento is None:
            view.botoes_atalhos.botao_sem_preenchimento.configure(image=self.img_botao_sem_preenchimento_ativo)
        else:
            view.botoes_atalhos.botao_sem_preenchimento.configure(image=self.img_botao_sem_preenchimento)

    # Atualiza o botão de cor de borda para a cor selecionada
    def atualiza_botao_borda(self, estado, view):
        view.botoes_atalhos.botao_cor_borda.configure(bg=estado.cor_borda)

    # Atualiza o botão de preenchimento para a cor selecionada ou volta para o cinza padrão
    def atualiza_botao_preenchimento(self, estado, view):
        if estado.cor_preenchimento is None:
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg="#C0C0C0")
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg=estado.cor_preenchimento)
        
        