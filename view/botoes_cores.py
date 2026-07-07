from tkinter import *

class BotoesCores:
    def __init__(self, root):
        # Botão Branco
        self.botao_branco = Button(
            master=root,
            bg="#FFFFFF",
            relief=RAISED,
            activebackground="#808080",
            boder=1)
        self.botao_branco.grid(row=0, column=0)

        # Botão Cinza
        self.botao_cinza = Button(
            master=root,
            bg="#8F8E8E",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_cinza.grid(row=0, column=1)

        #Botão Preto
        self.botao_preto = Button(
            master=root,
            bg="#000000",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_preto.grid(row=0, column=2)