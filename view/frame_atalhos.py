from tkinter import *

from view.botoes_atalhos import BotoesAtalhos

class FrameAtalhos:
    def __init__(self, root):
        self.frame = Frame(root, bg="#C0C0C0", width=100, height=250)
        self.frame.pack(padx=10)

        # Colocando os botões de atalhos
        self.botoes_formas = BotoesAtalhos(self.frame)