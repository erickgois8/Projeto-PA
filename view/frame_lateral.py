from tkinter import *

from view.frame_ferramentas import FrameFerramentas
from view.frame_formas import FrameFormas
from view.frame_cores import FrameCores
from view.frame_atalhos import FrameAtalhos

class FrameLateral:
    def __init__(self, root):
        # Frame principal próprio
        self.frame = Frame(root, bg="#C0C0C0", width=119)
        self.frame.pack(side=LEFT, fill=Y)

        # Frame de ferramentas
        self.frame_ferramentas = FrameFerramentas(self.frame)

        # Frame de formas
        self.frame_formas = FrameFormas(self.frame)

        # Frame de cores
        self.frame_cores = FrameCores(self.frame)

        # Frame de atalhos
        self.frame_atalhos = FrameAtalhos(self.frame)