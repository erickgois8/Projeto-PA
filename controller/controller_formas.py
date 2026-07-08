class ControladorFormas:
    def __init__(self, controlador_principal):
        self.controlador = controlador_principal
        self.janela = controlador_principal.janela

        self.configurar_botoes()

    def configurar_botoes(self):
        botoes_formas = self.janela.frame_lateral.frame_formas.botoes_formas

        # Botão de linha
        botoes_formas.botao_linha.config(
            command=lambda: self.seleciona_forma("linha"))
        
        # Botão de círculo
        botoes_formas.botao_circulo.config(
            command=lambda: self.seleciona_forma("circulo"))
        
        # Botão de oval
        botoes_formas.botao_oval.config(
            command=lambda: self.seleciona_forma("oval"))
        
        # Botão de quadrado
        botoes_formas.botao_quadrado.config(
            command=lambda: self.seleciona_forma("quadrado"))

        # Botão de retângulo
        botoes_formas.botao_retangulo.config(
            command=lambda: self.seleciona_forma("retangulo"))

    def seleciona_forma(self, forma):
        self.controlador.forma_atual = forma
        print("forma atual:", forma) #tirar dps