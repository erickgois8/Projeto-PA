from tkinter import *

from view.botoes_cores import BotoesCores

class FrameCores:
    def __init__(self, root):
        self.frame = Frame(root, bg="#C0C0C0", width=99, height=137)
        self.frame.pack(padx=10, pady=(0, 30))

        # Colocando os botões de cores
        self.botoes_formas = BotoesCores(self.frame)