from view.janela import Janela
from controller.controller_principal import ControllerPrincipal
from controller.controller_botoes import ControllerBotoes

janela = Janela()
controller_principal = ControllerPrincipal(janela)
controller_botoes = ControllerBotoes(janela, controller_principal)
janela.root.mainloop()