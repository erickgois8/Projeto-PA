class ControladorFerramentas:
    def __init__(self, controlador_principal):
        self.controlador = controlador_principal
        self.janela = controlador_principal.janela

        self.configurar_botoes()

    def configurar_botoes(self):
        botoes_ferramentas = self.janela.frame_lateral.frame_ferramentas.botoes_ferramentas

        # Botão de lápis
        botoes_ferramentas.botao_lapis.config(
            command=lambda: self.selecionar_ferramenta("lapis"))
        
        # Botão de borracha
        botoes_ferramentas.botao_borracha.config(
            command=lambda: self.selecionar_ferramenta("borracha"))
        
        # Botão de bade de tinta
        botoes_ferramentas.botao_balde_tinta.config(
            command=lambda: self.selecionar_ferramenta("balde_tinta"))

    def selecionar_ferramenta(self, ferramenta):
        self.controlador.ferramenta_atual = ferramenta
        print("Ferramenta atual:", ferramenta) #tirar dps