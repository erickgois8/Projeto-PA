from tkinter import *
from view.botoes_salvar import BotoesSalvar

class FrameSuperior:
    def __init__(self, root):
        # Frame superior
        self.frame = Frame(root, bg="#C0C0C0", height=50, relief=RAISED, bd=1)
        self.frame.pack(side=TOP, fill=X)

        # Colocando os botões de salvar e abrir
        self.botoes_salvar = BotoesSalvar(self.frame)