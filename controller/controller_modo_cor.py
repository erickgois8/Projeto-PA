from model.cores import Cores
from view.janela import Janela

class ControllerModoCor:
    def __init__(self, view: Janela, cores: Cores):
        botoes_atalhos = view.frame_lateral.frame_atalhos.botoes_atalhos

        # Botão cor da borda
        botoes_atalhos.btn_cor_borda.config(
            command=lambda: cores.selecionar_modo("borda"))

        # Botão figura preenchida
        botoes_atalhos.btn_fig_preenchida.config(
            command=lambda: cores.selecionar_modo("preenchimento"))

        # Botão retira preenchimento
        botoes_atalhos.btn_figura_vazia.config(
            command=lambda: cores.selecionar_modo("preenchimento"))
        
        
    # Atualiza o botão de cor de borda para a cor selecionada
    def atualiza_botao_borda(self, cor_borda):
        if cor_borda is None:
            self.btn_fig_borda.configure(bg="#808080")
        else:
            self.btn_fig_borda.configure(bg=cor_borda)

    # Atualiza o botão de preenchimento para a cor selecionada ou volta para o cinza padrão
    def atualiza_botao_preenchimento(self, cor_preenchimento):
        if cor_preenchimento is None:
            self.btn_fig_preenchida.configure(bg="#808080")
            self.btn_fig_preenchida.configure(bg=cor_preenchimento)

    # Atualiza o botão de sem preenchimento para que fique ativo quando selecionado e inativo quando não
    def atualiza_botao_sem_preenchimento(self, cor_preenchimento):
        if cor_preenchimento is None:
            self.btn_sem_preenchimento.configure(image=self.img_btn_sem_preenchimento_ativo)
        else:
            self.btn_sem_preenchimento.configure(image=self.img_btn_sem_preenchimento)