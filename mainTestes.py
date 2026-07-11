from view.janela import Janela
from controller.controller_principal import ControllerPrincipal

janela = Janela()
controlador = ControllerPrincipal(janela)

janela.root.mainloop()