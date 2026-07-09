from view.janela import Janela
from controller.controller_principal import ControladorPrincipal

janela = Janela()
controlador = ControladorPrincipal(janela)

janela.root.mainloop()
