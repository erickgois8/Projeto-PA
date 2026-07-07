from tkinter import *

class AreaDesenho:
    def __init__(self, root):
        self.canvas = Canvas(root, bg="#FFFFFF")
        self.canvas.pack(expand=TRUE, fill=BOTH)