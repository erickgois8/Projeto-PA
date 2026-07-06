from tkinter import *
from view.frame_ferramentas import FrameFerramentas
from view.frame_formas import FrameFormas
from view.frame_cores import FrameCores
from view.frame_atalhos import FrameAtalhos

class FrameLateral:
    def __init__(self, root):
        # Frame principal próprio
        self.frame = Frame(root, bg="#C0C0C0", width=120)

        # Colocando os outros frames
        self.frame_ferramentas = FrameFerramentas(self.frame)
        self.frame_ferramentas.pack()

        self.frame_formas = FrameFormas(self.frame)
        self.frame_formas.pack()

        self.frame_cores = FrameCores(self.frame)
        self.frame_cores.pack()