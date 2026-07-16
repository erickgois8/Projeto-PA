from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

class ControllerBotoesFormas:
   def __init__(self, view: Janela, controller: ControllerPrincipal):
      # Botão linha
      view.botoes_formas.botao_linha.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_linha, "crosshair"))

      # Botão círculo
      view.botoes_formas.botao_circulo.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_circulo, "crosshair"))

      # Botão oval
      view.botoes_formas.botao_oval.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_oval, "crosshair"))
      
      # Botão quadrado
      view.botoes_formas.botao_quadrado.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_quadrado, "crosshair"))
      
      # Botão retangulo
      view.botoes_formas.botao_retangulo.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_retangulo, "crosshair"))

      # Botão triangulo
      view.botoes_formas.botao_triangulo.configure(command=lambda: controller.selecionar_ferramenta(controller.ferramenta_triangulo, "crosshair"))

   def trocar_cursor(self, cursor):
      return
