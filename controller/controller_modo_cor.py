from view.janela import Janela
from model.estado import Estado

class ControllerModoCor:
    def __init__(self, view: Janela, estado: Estado):
    
        # Botão cor da borda
        view.botoes_atalhos.botao_cor_borda.configure(
            command=lambda: self.trocar_modo_cor(estado, view, "borda"))

        # Botão figura preenchida
        view.botoes_atalhos.botao_cor_preenchimento.configure(
            command=lambda: self.trocar_modo_cor(estado, view, "preenchimento"))

        # Botão retira preenchimento
        view.botoes_atalhos.botao_sem_preenchimento.configure(
            command=lambda: self.trocar_modo_cor(estado, view, "preenchimento"))
        
    # Junta as funções de atualizar botão de cor de borda e de preenchimento
    def trocar_modo_cor(self, estado, view, modo_cor):
        estado.selecionar_modo_cor(modo_cor)
        
        self.atualiza_botao_borda(estado, view)
        self.atualiza_botao_preenchimento(estado, view)
        
    # Atualiza o botão de cor de borda para a cor selecionada
    def atualiza_botao_borda(self, estado, view):
        view.botoes_atalhos.botao_cor_borda.configure(bg=estado.cor_borda)

    # Atualiza o botão de preenchimento para a cor selecionada ou volta para o cinza padrão
    def atualiza_botao_preenchimento(self, estado, view):
        if estado.cor_preenchimento is None:
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg="#C0C0C0")
            view.botoes_atalhos.botao_cor_preenchimento.configure(bg=estado.cor_preenchimento)