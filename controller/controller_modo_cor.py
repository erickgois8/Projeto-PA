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