from tkinter import *

class AreaDesenho:
    def __init__(self, root):
        self.canvas = Canvas(root, bg="#000000", width= 1770, height=1080)
        self.canvas.pack(side= RIGHT, expand=TRUE)