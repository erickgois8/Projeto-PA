from tkinter import *
from view.botoes_ferramentas import BotoesFerramentas

# Define o frame ferramentas
class FrameFerramentas:
    def __init__(self, root):
        self.frame = Frame(root, bg="#C0C0C0", width=99, height=67)
        self.frame.pack(padx=10, pady=(25, 60))

        # Colocando os botões de ferramentas
        self.botoes_ferramentas = BotoesFerramentas(self.frame)
        