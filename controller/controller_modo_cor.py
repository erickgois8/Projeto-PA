from view.janela import Janela
from model.estado import Estado
from tkinter import *

class ControllerModoCor:
    def __init__(self, view: Janela, estado: Estado):
        self.img_botao_sem_preenchimento_ativo = PhotoImage(file="images/sem_preenchimento_ativo.png")
        self.img_botao_sem_preenchimento = PhotoImage(file="images/sem_preenchimento.png")

        # Botão cor da borda
        view.botoes_atalhos.botao_cor_borda.configure(command=lambda: self.trocar_modo_cor(view, estado, "borda"))

        # Botão figura preenchida
        view.botoes_atalhos.botao_cor_preenchimento.configure(command=lambda: self.trocar_modo_cor(view, estado, "preenchimento"))

        # Botão retira preenchimento
        view.botoes_atalhos.botao_sem_preenchimento.configure(command=lambda: self.limpar_preenchimento(view, estado))

    def limpar_preenchimento(self, view: Janela, estado: Estado):
        estado.limpar_cor()
        
        self.atualiza_botao_sem_preenchimento(view, estado)
        self.atualiza_botao_preenchimento(view, estado)

    # Junta as funções de atualizar botão de cor de borda e de preenchimento
    def trocar_modo_cor(self, view: Janela, estado: Estado, modo_cor: str):
        estado.selecionar_modo_cor(modo_cor)
        
        self.atualiza_botao_borda(view, estado)
        self.atualiza_botao_preenchimento(view, estado)
        
    # Atualiza o botão de cor de borda para a cor selecionada
    def atualiza_botao_borda(self, view: Janela, estado: Estado):
        view.botoes_atalhos.botao_cor_borda.configure(bg=estado.cor_borda)

    # Atualiza o botão de preenchimento para a cor selecionada ou volta para o cinza padrão
    def atualiza_botao_preenchimento(self, view: Janela, estado: Estado):
        if estado.cor_preenchimento is None:
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg="#C0C0C0")
        else:
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg=estado.cor_preenchimento)

    def atualiza_botao_sem_preenchimento(self, view: Janela, estado: Estado):
        if estado.cor_preenchimento is None:
            view.botoes_atalhos.botao_sem_preenchimento.configure(image=self.img_botao_sem_preenchimento_ativo)
        else:
            view.botoes_atalhos.botao_sem_preenchimento.configure(image=self.img_botao_sem_preenchimento)