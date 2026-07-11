from tkinter import *
from view.botoes_cores import BotoesCores

# Define frame de botões de cores
class FrameCores:
    def __init__(self, frame_lateral):
        self.frame = Frame(frame_lateral, bg="#C0C0C0", width=99, height=137)
        self.frame.pack(padx=10, pady=(0, 30))

        # Colocando os botões de cores
        self.botoes_cores = BotoesCores(self.frame)