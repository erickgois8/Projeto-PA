from tkinter import *

from view.botoes_atalhos import BotoesAtalhos

class FrameAtalhos:
    def __init__(self, frame_lateral):
        self.frame = Frame(frame_lateral, bg="#C0C0C0", width=99, height=231)
        self.frame.pack(padx=10)

        # Colocando os botões de atalhos
        
        self.botoes_atalhos = BotoesAtalhos(self.frame)