from tkinter import *

class FrameFerramentas:
    def __init__(self, root):
        self.frame = Frame(root, bg="#C0C0C0", width=100, height=67)
        self.frame.pack(padx=10, pady=(25, 60))

        # Botões de ferramentas
        