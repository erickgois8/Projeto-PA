from view.janela import Janela
from model.estado import Estado

class ControllerFormas:
     def __init__(self, view: Janela, estado: Estado):
        # Botão linha
        view.botoes_formas.botao_linha.configure(
            command=lambda: estado.selecionar_ferramenta("linha"))

        # Botão círculo
        view.botoes_formas.botao_circulo.configure(
            command=lambda: estado.selecionar_ferramenta("circulo"))

        # Botão oval
        view.botoes_formas.botao_oval.configure(
            command=lambda: estado.selecionar_ferramenta("oval"))
        
        # Botão quadrado
        view.botoes_formas.botao_quadrado.configure(
            command=lambda: estado.selecionar_ferramenta("quadrado"))
        
        # Botão retangulo
        view.botoes_formas.botao_retangulo.configure(
            command=lambda: estado.selecionar_ferramenta("retangulo"))