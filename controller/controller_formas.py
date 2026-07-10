from model.ferramentas import Ferramentas
from view.janela import Janela

class ControllerFormas:
     def __init__(self, view: Janela, ferramentas: Ferramentas):

        # Botão linha
        view.frame_lateral.frame_formas.botoes_formas.botao_linha.config(
            command=lambda: ferramentas.selecionar_ferramenta("linha"))

        # Botão cículo
        view.frame_lateral.frame_formas.botoes_formas.botao_circulo.config(
            command=lambda: ferramentas.selecionar_ferramenta("circulo"))

        # Botão oval
        view.frame_lateral.frame_formas.botoes_formas.botao_oval.config(
            command=lambda: ferramentas.selecionar_ferramenta("oval"))
        
        # Botão quadrado
        view.frame_lateral.frame_formas.botoes_formas.botao_quadrado.config(
            command=lambda: ferramentas.selecionar_ferramenta("quadrado"))
        
        # Botão retangulo
        view.frame_lateral.frame_formas.botoes_formas.botao_retangulo.config(
            command=lambda: ferramentas.selecionar_ferramenta("retangulo"))
        
        # Botão triangulo
        view.frame_lateral.frame_formas.botoes_formas.botao_triangulo.config(
            command=lambda: ferramentas.selecionar_ferramenta("triangulo"))