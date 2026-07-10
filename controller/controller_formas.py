from model.ferramentas import Ferramentas
from view.janela import Janela

class ControlleFerramentas:
     def __init__(self, view: Janela, ferramentas: Ferramentas):
        botoes_ferramentas = view.frame_lateral.frame_ferramentas.botoes_ferramentas

        # Botão linha
        botoes_ferramentas.botao_linha.config(
            command=lambda: ferramentas.selecionar_ferramenta("linha"))

        # Botão cículo
        botoes_ferramentas.botao_circulo.config(
            command=lambda: ferramentas.selecionar_ferramenta("circulo"))

        # Botão oval
        botoes_ferramentas.botao_oval.config(
            command=lambda: ferramentas.selecionar_ferramenta("oval"))
        
        # Botão quadrado
        botoes_ferramentas.botao_quadrado.config(
            command=lambda: ferramentas.selecionar_ferramenta("quadrado"))
        
        # Botão retangulo
        botoes_ferramentas.botao_retangulo.config(
            command=lambda: ferramentas.selecionar_ferramenta("retangulo"))
        
        # Botão triangulo
        botoes_ferramentas.botao_triangulo.config(
            command=lambda: ferramentas.selecionar_ferramenta("triangulo"))