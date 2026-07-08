class ConfigFerramentas:
    def __init__(self, controlador_ferramentas):
        self.controlador_ferramentas = controlador_ferramentas
        self.janela = controlador_ferramentas.janela

        botoes_ferramentas = self.janela.frame_lateral.frame_ferramentas.botoes_ferramentas

        # Botão de lápis
        botoes_ferramentas.botao_lapis.config(
            command=lambda: self.selecionar_ferramenta("lapis"))

        # Botão de borracha
        botoes_ferramentas.botao_borracha.config(
            command=lambda: self.selecionar_ferramenta("borracha"))

        # Botão de balde de tinta
        botoes_ferramentas.botao_balde_tinta.config(
            command=lambda: self.selecionar_ferramenta("balde_tinta"))

    def selecionar_ferramenta(self, ferramenta):
        self.controlador_ferramentas.selecionar_ferramenta(ferramenta)
        print("Ferramenta atual:", ferramenta)  # tirar dps