from tkinter import *

from view.botoes_formas import BotoesFormas

class FrameFormas:
    def __init__(self, frame_lateral):
        self.frame = Frame(frame_lateral, bg="#C0C0C0", width=99, height=102)
        self.frame.pack(padx=10, pady=(0, 350))

        # Colocando os botões de formas
        self.botoes_formas = BotoesFormas(self.frame)