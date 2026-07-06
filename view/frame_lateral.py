from tkinter import *
from frame_ferramentas import FrameFerramentas
from frame_formas import FrameFormas
from frame_cores import FrameCores
from frame_atalhos import FrameAtalhos

class FrameLateral:
    def __init__(self, root):
        self.frame = Frame(root, bg="#C0C0C0", width=120, height=1080)