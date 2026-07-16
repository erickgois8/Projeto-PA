from view.janela import Janela
from controller.controller_principal import ControllerPrincipal
from tkinter import *

class ControllerBotoesModoCor:
    def __init__(self, view: Janela, controller: ControllerPrincipal):
        self.img_botao_sem_preenchimento_ativo = PhotoImage(file="images/sem_preenchimento_ativo.png")
        self.img_botao_sem_preenchimento = PhotoImage(file="images/sem_preenchimento.png")

        # Botão cor da borda
        view.botoes_atalhos.botao_cor_borda.configure(command=lambda: self.trocar_modo_cor(view, controller, "borda"))

        # Botão figura preenchida
        view.botoes_atalhos.botao_cor_preenchimento.configure(command=lambda: self.trocar_modo_cor(view, controller, "preenchimento"))

        # Botão retira preenchimento
        view.botoes_atalhos.botao_sem_preenchimento.configure(command=lambda: self.limpar_preenchimento(view, controller))











    # Método para limpar a cor de preenchimento da figura selecionada
    def limpar_preenchimento(self, view: Janela, controller: ControllerPrincipal):
        controller.estado.limpar_cor()
        
        self.atualiza_botao_sem_preenchimento(view, controller)
        self.atualiza_botao_preenchimento(view, controller)

    # Método para trocar o modo de cor (borda ou preenchimento) da figura selecionada
    def trocar_modo_cor(self, view: Janela, controller: ControllerPrincipal, modo_cor: str):
        controller.estado.selecionar_modo_cor(modo_cor)
        
        self.atualiza_botao_borda(view, controller)
        self.atualiza_botao_preenchimento(view, controller)











# -------------------- MÉTODOS AUXILIARES -------------------- #

    # Atualiza o botão de cor de borda para a cor selecionada
    def atualiza_botao_borda(self, view: Janela, controller: ControllerPrincipal):
        view.botoes_atalhos.botao_cor_borda.configure(bg=controller.estado.cor_borda)

    # Atualiza o botão de preenchimento para a cor selecionada ou volta para o cinza padrão
    def atualiza_botao_preenchimento(self, view: Janela, controller: ControllerPrincipal):
        if controller.estado.cor_preenchimento is None:
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg="#C0C0C0")
        else:
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg=controller.estado.cor_preenchimento)

    def atualiza_botao_sem_preenchimento(self, view: Janela, controller: ControllerPrincipal):
        if controller.estado.cor_preenchimento is None:
            view.botoes_atalhos.botao_sem_preenchimento.configure(image=self.img_botao_sem_preenchimento_ativo)
        else:
            view.botoes_atalhos.botao_sem_preenchimento.configure(image=self.img_botao_sem_preenchimento)

    def trocar_cursor(self, cursor):
        return