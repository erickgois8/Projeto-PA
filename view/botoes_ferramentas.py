from tkinter import *

class BotoesFerramentas:
    def __init__(self, root):

        # Imagens dos Botões
        self.img_btn_lapis = PhotoImage(file="images/lapis.png")
        self.img_btn_borracha = PhotoImage(file="images/borracha.png")
        self.img_btn_balde_tinta = PhotoImage(file="images/balde_tinta.png")

        # Botão de Lápis
        self.botao_lapis = Button(
            master=root,
            image=self.img_btn_lapis,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_lapis.grid(row=0, column=0)
    
        # Botão de Borracha
        self.botao_borracha = Button(
            master=root,
            image=self.img_btn_borracha,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_borracha.grid(row=0, column=1)

        # Botão de Balde de Tinta
        self.botao_balde_tinta = Button(
            master=root,
            image=self.img_btn_balde_tinta,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_balde_tinta.grid(row=0, column=2)