from tkinter import *
from view.frame_ferramentas import FrameFerramentas
from view.frame_formas import FrameFormas
from view.frame_cores import FrameCores
from view.frame_atalhos import FrameAtalhos

class FrameLateral:
    def __init__(self, root):
        # Frame principal próprio
        self.frame = Frame(root, bg="#C0C0C0", width=140, height=1080)
        self.frame.pack(side= LEFT, fill= BOTH)