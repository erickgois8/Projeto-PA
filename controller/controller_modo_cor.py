from view.janela import Janela
from model.estado import Estado

class ControllerModoCor:
    def __init__(self, view: Janela, estado: Estado):
        # Botão cor da borda
        view.botoes_atalhos.botao_cor_borda.configure(
            command=lambda: estado.selecionar_modo_cor("borda"))

        # Botão figura preenchida
        view.botoes_atalhos.botao_cor_preenchimento.configure(
            command=lambda: estado.selecionar_modo_cor("preenchimento"))

        # Botão retira preenchimento
        view.botoes_atalhos.botao_sem_preenchimento.configure(
            command=lambda: estado.selecionar_modo_cor("preenchimento"))
        
    # Atualiza o botão de cor de borda para a cor selecionada
    def atualiza_botao_borda(self, cor_borda):
        if cor_borda is "":
            self.btn_fig_borda.configure(bg="#808080")
        else:
            self.btn_fig_borda.configure(bg=cor_borda)

    # Atualiza o botão de preenchimento para a cor selecionada ou volta para o cinza padrão
    def atualiza_botao_preenchimento(self, cor_preenchimento):
        if cor_preenchimento is "":
            self.btn_fig_preenchida.configure(bg="#808080")
            self.btn_fig_preenchida.configure(bg=cor_preenchimento)

    # Atualiza o botão de sem preenchimento para que fique ativo quando selecionado e inativo quando não
    def atualiza_botao_sem_preenchimento(self, cor_preenchimento):
        if cor_preenchimento is "":
            self.btn_sem_preenchimento.configure(image=self.img_btn_sem_preenchimento_ativo)
        else:
            self.btn_sem_preenchimento.configure(image=self.img_btn_sem_preenchimento)